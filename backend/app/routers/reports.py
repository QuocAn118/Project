from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from ..auth import require_role
from datetime import datetime

router = APIRouter()


@router.get('/summary')
def summary(start: str | None = None, end: str | None = None, group_by: str = 'department', db: Session = Depends(get_db), admin = Depends(require_role('admin'))):
    q = db.query(models.Message)
    if start:
        try:
            sdt = datetime.fromisoformat(start)
            q = q.filter(models.Message.received_at >= sdt)
        except Exception:
            pass
    if end:
        try:
            edt = datetime.fromisoformat(end)
            q = q.filter(models.Message.received_at <= edt)
        except Exception:
            pass

    messages = q.all()
    result = {}
    if group_by == 'department':
        # map messages to departments by keyword
        for m in messages:
            dept_name = 'unknown'
            if m.keywords:
                # take first keyword -> find dept
                first = m.keywords.split(',')[0]
                kw = db.query(models.Keyword).filter(models.Keyword.word==first).first()
                if kw and kw.department:
                    dept_name = kw.department.name
            result.setdefault(dept_name, 0)
            result[dept_name] += 1
    elif group_by == 'user':
        for m in messages:
            uid = m.assigned_to or 'unassigned'
            result.setdefault(str(uid), 0)
            result[str(uid)] += 1
    else:
        result['total'] = len(messages)

    return {"count": len(messages), "by": group_by, "buckets": result}
