from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import WebhookMessage
from .. import models
from ..services.assignment import process_message_and_assign

router = APIRouter()

@router.post('/')
def receive_webhook(payload: WebhookMessage, db: Session = Depends(get_db)):
    # persist raw message
    msg = models.Message(platform=payload.platform, sender=payload.sender, content=payload.content)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    # process keywords and assignment
    keywords, assigned_user = process_message_and_assign(db, msg)
    msg.keywords = ",".join(keywords)
    msg.assigned_to = assigned_user.id if assigned_user else None
    db.add(msg)
    db.commit()
    return {"message_id": msg.id, "keywords": keywords, "assigned_to": assigned_user.username if assigned_user else None}
