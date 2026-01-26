from __future__ import annotations

from sqlalchemy.orm import Session

from app import models, schemas


def create_organization(
    db: Session,
    org: schemas.OrganizationCreate,
) -> models.Organization:
    db_org = models.Organization(
        name=org.name,
        description=org.description,
    )
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org


def get_organization(db: Session, org_id: int) -> models.Organization | None:
    return db.query(models.Organization).filter(models.Organization.id == org_id).first()
