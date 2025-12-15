from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..auth import get_current_user
from .. import models
from ..schemas import MessageOut
from typing import List

router = APIRouter()

@router.get('/', response_model=List[MessageOut])
def list_messages(db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    msgs = db.query(models.Message).order_by(models.Message.received_at.desc()).limit(200).all()
    return msgs

@router.post('/{message_id}/complete')
def complete_message(message_id: int, db: Session = Depends(get_db), user: models.User = Depends(get_current_user)):
    msg = db.query(models.Message).filter(models.Message.id==message_id).first()
    if not msg:
        return {"error": "not found"}
    # mark assignment complete
    assignment = db.query(models.Assignment).filter(models.Assignment.message_id==message_id, models.Assignment.user_id==user.id).first()
    if assignment:
        assignment.status = 'closed'
        user.status = models.StatusEnum.available
        db.add(assignment)
        db.add(user)
        db.commit()
        return {"ok": True}
    return {"error": "no assignment for user"}
