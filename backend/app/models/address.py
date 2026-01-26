from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .party_address import PartyAddress


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(20), nullable=False)

    parties: Mapped[List["PartyAddress"]] = relationship(
        "PartyAddress",
        back_populates="address",
        cascade="all, delete-orphan",
    )

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "address",
    }


class GeoAddress(Address):
    __tablename__ = "geo_address"

    id: Mapped[int] = mapped_column(ForeignKey("address.id"), primary_key=True)
    street: Mapped[Optional[str]] = mapped_column(String(255))
    city: Mapped[Optional[str]] = mapped_column(String(100))
    zip_code: Mapped[Optional[str]] = mapped_column(String(20))
    country: Mapped[Optional[str]] = mapped_column(String(100))
    latitude: Mapped[Optional[float]] = mapped_column(Float)
    longitude: Mapped[Optional[float]] = mapped_column(Float)

    __mapper_args__ = {
        "polymorphic_identity": "GEO",
    }


class TeleAddress(Address):
    __tablename__ = "tele_address"

    id: Mapped[int] = mapped_column(ForeignKey("address.id"), primary_key=True)
    medium_type: Mapped[str] = mapped_column(String(50), nullable=False)
    value: Mapped[str] = mapped_column(String(255), nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "TELE",
    }
