from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .party_address import PartyAddress


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    street: Mapped[Optional[str]] = mapped_column(String(255))
    city: Mapped[Optional[str]] = mapped_column(String(100))
    zip_code: Mapped[Optional[str]] = mapped_column(String(20))
    country: Mapped[Optional[str]] = mapped_column(String(100))

    parties: Mapped[List["PartyAddress"]] = relationship(
        "PartyAddress",
        back_populates="address",
        cascade="all, delete-orphan",
    )
