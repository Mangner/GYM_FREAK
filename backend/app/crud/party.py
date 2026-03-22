from __future__ import annotations

from sqlalchemy.orm import Session

from app import models


def get_party(db: Session, party_id: int) -> models.Party | None:
    return db.query(models.Party).filter(models.Party.id == party_id).first()
