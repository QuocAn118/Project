from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from ..auth import get_current_user, require_role

router = APIRouter()

@router.get('/user')
def get_user_kpi(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    metrics = db.query(models.KPIMetric).filter(models.KPIMetric.user_id==user.id).order_by(models.KPIMetric.period.desc()).limit(12).all()
    return {"user": user.full_name, "metrics": metrics}

@router.get('/department')
def get_dept_kpi(db: Session = Depends(get_db), manager = Depends(require_role('manager,admin'))):
    metrics = db.query(models.KPIMetric).filter(models.KPIMetric.user_id.in_([u.id for u in db.query(models.User).filter(models.User.role==models.RoleEnum.staff).all()])).all()
    return {"metrics": metrics}

@router.post('/record')
def record_kpi(user_id: int, metric_name: str, metric_value: float, period: str, db: Session = Depends(get_db), admin = Depends(require_role('admin'))):
    kpi = models.KPIMetric(user_id=user_id, metric_name=metric_name, metric_value=metric_value, period=period)
    db.add(kpi)
    db.commit()
    return {"ok": True}
