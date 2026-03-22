from __future__ import annotations

from sqlalchemy.orm import Session

from app import models, schemas


def create_person(db: Session, person: schemas.PersonCreate) -> models.Person:
    db_person = models.Person(
        first_name=person.first_name,
        last_name=person.last_name,
        gender=person.gender,
        birth_date=person.birth_date,
        username=person.username,
        email=person.email,
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def get_person(db: Session, person_id: int) -> models.Person | None:
    return db.query(models.Person).filter(models.Person.id == person_id).first()


def get_person_by_username(db: Session, username: str) -> models.Person | None:
    return db.query(models.Person).filter(models.Person.username == username).first()
