import json
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from fastapi import APIRouter
from app.crud import create_message
from app.schemas import Payload

router = APIRouter(tags=["Hello"])


@router.post("/hello_post")
def hello_post(payload: Payload, db: Session = Depends(get_db)):
    res = create_message(db, payload)
    print(res)
    return {"data": res}


@router.get("/hello_get")
def hello_get():
    return {"response": "Hi"}


