from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from ..auth import get_current_user, require_role

router = APIRouter()

@router.get('/', response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db), admin = Depends(require_role('admin'))):
    return db.query(models.User).all()

@router.post('/', response_model=schemas.UserOut)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db), admin = Depends(require_role('admin'))):
    from ..auth import get_password_hash
    hashed = get_password_hash(user_in.password)
    user = models.User(username=user_in.username, full_name=user_in.full_name, hashed_password=hashed, role=user_in.role, department_id=user_in.department_id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.put('/{user_id}/status')
def set_status(user_id: int, status: str, db: Session = Depends(get_db), manager = Depends(require_role('manager'))):
    u = db.query(models.User).filter(models.User.id==user_id).first()
    if not u:
        raise HTTPException(404)
    u.status = status
    db.add(u)
    db.commit()
    return {"ok": True}
