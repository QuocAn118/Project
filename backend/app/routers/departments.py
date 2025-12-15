from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from ..auth import require_role, get_current_user

router = APIRouter()


@router.get('/', response_model=list[schemas.DepartmentOut])
def list_departments(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    return db.query(models.Department).all()


@router.post('/', response_model=schemas.DepartmentOut)
def create_department(dep: schemas.DepartmentOut, db: Session = Depends(get_db), admin = Depends(require_role('admin'))):
    d = models.Department(name=dep.name)
    db.add(d)
    db.commit()
    db.refresh(d)
    return d
