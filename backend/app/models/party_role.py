from __future__ import annotations

from datetime import date
from typing import Optional, TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .party import Party


class PartyRole(Base):
    __tablename__ = "party_role"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    party_id: Mapped[int] = mapped_column(ForeignKey("party.id"), nullable=False)
    type: Mapped[str] = mapped_column(String(50), nullable=False)
    active_from: Mapped[Optional[date]] = mapped_column(Date)
    active_to: Mapped[Optional[date]] = mapped_column(Date)

    party: Mapped["Party"] = relationship("Party", back_populates="roles")
