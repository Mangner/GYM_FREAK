from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.PersonRead, status_code=status.HTTP_201_CREATED)
def create_person(
    person: schemas.PersonCreate,
    db: Session = Depends(get_db),
) -> schemas.PersonRead:
    return crud.create_person(db, person)


@router.get("/{person_id}", response_model=schemas.PersonRead)
def get_person(
    person_id: int,
    db: Session = Depends(get_db),
) -> schemas.PersonRead:
    db_person = crud.get_person(db, person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person
