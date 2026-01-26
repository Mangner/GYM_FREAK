from __future__ import annotations

from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .party import Party


class Organization(Party):
    __tablename__ = "organization"

    id: Mapped[int] = mapped_column(ForeignKey("party.id"), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(500))

    __mapper_args__ = {
        "polymorphic_identity": "ORGANIZATION",
    }
