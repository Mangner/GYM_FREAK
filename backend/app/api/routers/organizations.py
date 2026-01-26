from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.OrganizationRead, status_code=status.HTTP_201_CREATED)
def create_organization(
    org: schemas.OrganizationCreate,
    db: Session = Depends(get_db),
) -> schemas.OrganizationRead:
    return crud.create_organization(db, org)


@router.get("/{org_id}", response_model=schemas.OrganizationRead)
def get_organization(
    org_id: int,
    db: Session = Depends(get_db),
) -> schemas.OrganizationRead:
    db_org = crud.get_organization(db, org_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_org
