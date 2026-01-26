from __future__ import annotations

from datetime import date
from typing import Optional

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .party import Party


class Person(Party):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(ForeignKey("party.id"), primary_key=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(100))
    last_name: Mapped[Optional[str]] = mapped_column(String(100))
    gender: Mapped[Optional[str]] = mapped_column(String(20))
    birth_date: Mapped[Optional[date]] = mapped_column(Date)

    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "person",
    }
