from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from ..auth import get_current_user, require_role
from datetime import datetime

router = APIRouter()

@router.post('/', response_model=schemas.RequestOut)
def create_request(payload: schemas.RequestCreate, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    req = models.Request(user_id=user.id, request_type=payload.request_type, description=payload.description)
    db.add(req)
    db.commit()
    db.refresh(req)
    return req

@router.get('/', response_model=list[schemas.RequestOut])
def list_requests(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    if user.role.value == 'staff':
        return db.query(models.Request).filter(models.Request.user_id==user.id).all()
    else:
        return db.query(models.Request).all()

@router.get('/pending')
def list_pending(db: Session = Depends(get_db), manager = Depends(require_role('manager,admin'))):
    return db.query(models.Request).filter(models.Request.status=='pending').all()

@router.post('/{req_id}/review')
def review_request(req_id: int, payload: schemas.RequestReview, db: Session = Depends(get_db), manager = Depends(require_role('manager,admin'))):
    req = db.query(models.Request).filter(models.Request.id==req_id).first()
    if not req:
        raise HTTPException(404)
    req.status = payload.status
    req.notes = payload.notes
    req.reviewed_at = datetime.utcnow()
    db.add(req)
    db.commit()
    return {"ok": True}
