from fastapi import FastAPI

from app.api import router as api_router
from app.database import Base, engine

app = FastAPI(title="Gym Freak API")


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


app.include_router(api_router)
