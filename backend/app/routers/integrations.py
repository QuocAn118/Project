from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class ZaloMessage(BaseModel):
    phone: str
    message: str
    timestamp: int

# Mock Zalo OA webhook handler
@router.post('/zalo/webhook')
def zalo_webhook(payload: ZaloMessage):
    """
    This endpoint simulates receiving messages from Zalo OA API.
    In production, verify webhook signature and parse actual Zalo format.
    """
    # In production: verify_zalo_signature(payload)
    # Forward to main webhook handler
    from ..routers.webhook import router as webhook_router
    # create message object and process
    msg_data = {
        "platform": "zalo",
        "sender": payload.phone,
        "content": payload.message
    }
    return {"status": "received", "message_id": 1}

class MetaMessage(BaseModel):
    phone: str
    text: str
    timestamp: int

@router.post('/meta/webhook')
def meta_webhook(payload: MetaMessage):
    """
    This endpoint simulates receiving messages from Meta Business Manager API.
    In production, verify webhook signature and parse actual Meta WhatsApp format.
    """
    # In production: verify_meta_signature(payload)
    msg_data = {
        "platform": "meta",
        "sender": payload.phone,
        "content": payload.text
    }
    return {"status": "received", "message_id": 1}
