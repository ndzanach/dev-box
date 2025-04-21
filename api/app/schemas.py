from typing import Optional
from pydantic import BaseModel


class Payload(BaseModel):
    message: str
    subject: Optional[str] = 'None'
    class Config:
        orm_mode = True
