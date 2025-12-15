from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from ..auth import get_current_user, require_role
from datetime import datetime

router = APIRouter()

@router.post('/', response_model=schemas.ShiftOut)
def create_shift(shift: schemas.ShiftOut, db: Session = Depends(get_db), manager = Depends(require_role('manager,admin'))):
    # Note: This endpoint expects dept_id to be provided as query param
    s = models.Shift(department_id=1, shift_name=shift.shift_name, start_time=shift.start_time, end_time=shift.end_time)
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

@router.get('/', response_model=list[schemas.ShiftOut])
def list_shifts(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    return db.query(models.Shift).all()

@router.post('/assign')
def assign_shift(payload: schemas.ShiftAssignmentCreate, db: Session = Depends(get_db), manager = Depends(require_role('manager,admin'))):
    sa = models.ShiftAssignment(user_id=payload.user_id, shift_id=payload.shift_id, assigned_date=payload.assigned_date)
    db.add(sa)
    db.commit()
    return {"ok": True}

@router.post('/checkin')
def check_in(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    from datetime import date
    today = str(date.today())
    tt = db.query(models.TimeTracking).filter(models.TimeTracking.user_id==user.id, models.TimeTracking.date==today).first()
    if not tt:
        tt = models.TimeTracking(user_id=user.id, date=today)
    tt.check_in_time = datetime.utcnow()
    user.status = models.StatusEnum.available
    db.add(tt)
    db.add(user)
    db.commit()
    return {"ok": True, "check_in": str(tt.check_in_time)}

@router.post('/checkout')
def check_out(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    from datetime import date
    today = str(date.today())
    tt = db.query(models.TimeTracking).filter(models.TimeTracking.user_id==user.id, models.TimeTracking.date==today).first()
    if tt:
        tt.check_out_time = datetime.utcnow()
        user.status = models.StatusEnum.offline
        db.add(tt)
        db.add(user)
        db.commit()
        return {"ok": True, "check_out": str(tt.check_out_time)}
    return {"error": "no check-in for today"}

@router.get('/timesheet')
def get_timesheet(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    records = db.query(models.TimeTracking).filter(models.TimeTracking.user_id==user.id).order_by(models.TimeTracking.date.desc()).limit(30).all()
    return records
