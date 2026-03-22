from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .party import Party


class PartyRelationship(Base):
    __tablename__ = "party_relationship"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    from_party_id: Mapped[int] = mapped_column(ForeignKey("party.id"), nullable=False)
    to_party_id: Mapped[int] = mapped_column(ForeignKey("party.id"), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    from_party: Mapped["Party"] = relationship(
        "Party",
        foreign_keys=[from_party_id],
        back_populates="outgoing_relationships",
    )
    to_party: Mapped["Party"] = relationship(
        "Party",
        foreign_keys=[to_party_id],
        back_populates="incoming_relationships",
    )
