from fastapi import FastAPI

from app.api import tasks
from app.core.database import engine
from app.core.dependencies import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.router)
