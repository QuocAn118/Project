from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from ..auth import require_role, get_current_user

router = APIRouter()


@router.get('/', response_model=list[schemas.KeywordOut])
def list_keywords(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    return db.query(models.Keyword).all()


@router.post('/', response_model=schemas.KeywordOut)
def create_keyword(payload: schemas.KeywordCreate, db: Session = Depends(get_db), manager = Depends(require_role('manager,admin'))):
    k = models.Keyword(word=payload.word, department_id=payload.department_id)
    db.add(k)
    db.commit()
    db.refresh(k)
    return k


@router.put('/{kid}', response_model=schemas.KeywordOut)
def update_keyword(kid: int, payload: schemas.KeywordCreate, db: Session = Depends(get_db), manager = Depends(require_role('manager,admin'))):
    k = db.query(models.Keyword).filter(models.Keyword.id==kid).first()
    if not k:
        raise HTTPException(404, 'not found')
    k.word = payload.word
    k.department_id = payload.department_id
    db.add(k)
    db.commit()
    db.refresh(k)
    return k


@router.delete('/{kid}')
def delete_keyword(kid: int, db: Session = Depends(get_db), manager = Depends(require_role('manager,admin'))):
    k = db.query(models.Keyword).filter(models.Keyword.id==kid).first()
    if not k:
        raise HTTPException(404, 'not found')
    db.delete(k)
    db.commit()
    return {"ok": True}
