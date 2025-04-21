from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime
from app.database import Base

class Messages(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(255))
    subject = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    