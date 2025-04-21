from app.models import Base
import logging
from fastapi import FastAPI
from app.routers import  ws, hello
from app.database import engine
from sqlalchemy.exc import OperationalError
import time

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

MAX_RETRIES = 10

@app.on_event("startup")
def startup_event():
    for i in range(MAX_RETRIES):
        try:
            print(f"Attempting DB connection... {i+1}/{MAX_RETRIES}")
            with engine.connect():
                Base.metadata.create_all(bind=engine)
                print("✅ Tables created successfully.")
                break
        except OperationalError as e:
            print(f"❌ DB not ready: {e}")
            time.sleep(3)
    else:
        print("❌ Failed to connect to DB after retries.")


app.include_router(hello.router, prefix="/api")
app.include_router(ws.ws_router)
