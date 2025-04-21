
from sqlalchemy.orm import Session
from app.schemas import Payload
from app.models import Messages

def create_message(db: Session, payload: Payload):
    db_payload = Messages(**payload.dict())
    db.add(db_payload)
    db.commit()
    db.refresh(db_payload)
    return db_payload
