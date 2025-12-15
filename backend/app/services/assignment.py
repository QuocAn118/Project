from sqlalchemy.orm import Session
from .. import models
from typing import List

def extract_keywords(db: Session, content: str) -> List[str]:
    # naive keyword extraction: match known keywords in DB
    words = set([w.strip().lower() for w in content.split() if len(w) > 2])
    db_keywords = db.query(models.Keyword).all()
    found = []
    for k in db_keywords:
        if k.word.lower() in content.lower() or k.word.lower() in words:
            found.append(k.word)
    return found


def select_staff_for_assignment(db: Session, keywords: List[str]):
    # simple heuristic: pick staff in departments linked to keywords with highest KPI and available
    if not keywords:
        # fallback: pick any available staff with highest KPI
        user = db.query(models.User).filter(models.User.role==models.RoleEnum.staff, models.User.status==models.StatusEnum.available).order_by(models.User.kpi_score.desc()).first()
        return user
    # find departments for keywords
    dept_ids = set()
    for kw in db.query(models.Keyword).filter(models.Keyword.word.in_(keywords)).all():
        if kw.department_id:
            dept_ids.add(kw.department_id)
    q = db.query(models.User).filter(models.User.role==models.RoleEnum.staff, models.User.status==models.StatusEnum.available)
    if dept_ids:
        q = q.filter(models.User.department_id.in_(dept_ids))
    user = q.order_by(models.User.kpi_score.desc()).first()
    return user


def process_message_and_assign(db: Session, message: models.Message):
    keywords = extract_keywords(db, message.content)
    user = select_staff_for_assignment(db, keywords)
    if user:
        # create assignment
        assign = models.Assignment(message_id=message.id, user_id=user.id)
        user.status = models.StatusEnum.busy
        db.add(assign)
        db.add(user)
        db.commit()
        db.refresh(user)
        return keywords, user
    return keywords, None
