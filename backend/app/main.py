from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models
from app.api.routers import organizations, parties, people
from app.database import engine

app = FastAPI(title="Gym Freak API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    models.Base.metadata.create_all(bind=engine)


@app.get("/")
def health_check() -> dict:
    return {"message": "Gym Freak API is ready!"}


app.include_router(people.router, prefix="/people", tags=["People"])
app.include_router(organizations.router, prefix="/organizations", tags=["Organizations"])
app.include_router(parties.router, prefix="/parties", tags=["Parties"])
