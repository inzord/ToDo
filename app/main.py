import logging
from fastapi import FastAPI

from app.api import tasks
from app.core.database import engine, Base, init_db
from app.core.settings import settings

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Include routers
app.include_router(tasks.router, prefix=settings.API_V1_STR, tags=["tasks"])


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up FastAPI application")
    #await init_db()


@app.get("/")
async def root():
    logger.info("Root endpoint called")
    return {
        "message": "Welcome to Task API",
        "version": settings.VERSION,
        "docs_url": "/docs"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
