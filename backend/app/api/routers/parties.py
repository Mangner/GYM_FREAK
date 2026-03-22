from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.get("/{party_id}", response_model=schemas.PartyRead)
def get_party(
    party_id: int,
    db: Session = Depends(get_db),
) -> schemas.PartyRead:
    db_party = crud.get_party(db, party_id)
    if db_party is None:
        raise HTTPException(status_code=404, detail="Party not found")
    return db_party
