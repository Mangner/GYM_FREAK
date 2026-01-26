from __future__ import annotations

from typing import List, TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .party_address import PartyAddress
    from .registered_identifier import RegisteredIdentifier
    from .party_role import PartyRole
    from .relationship import PartyRelationship


class Party(Base):
    __tablename__ = "party"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(50), nullable=False)

    addresses: Mapped[List["PartyAddress"]] = relationship(
        "PartyAddress",
        back_populates="party",
        cascade="all, delete-orphan",
    )
    identifiers: Mapped[List["RegisteredIdentifier"]] = relationship(
        "RegisteredIdentifier",
        back_populates="party",
        cascade="all, delete-orphan",
    )
    roles: Mapped[List["PartyRole"]] = relationship(
        "PartyRole",
        back_populates="party",
        cascade="all, delete-orphan",
    )
    outgoing_relationships: Mapped[List["PartyRelationship"]] = relationship(
        "PartyRelationship",
        foreign_keys="PartyRelationship.from_party_id",
        back_populates="from_party",
        cascade="all, delete-orphan",
    )
    incoming_relationships: Mapped[List["PartyRelationship"]] = relationship(
        "PartyRelationship",
        foreign_keys="PartyRelationship.to_party_id",
        back_populates="to_party",
        cascade="all, delete-orphan",
    )

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "party",
    }
