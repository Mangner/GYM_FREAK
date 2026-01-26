from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from .address import Address
    from .party import Party


class PartyAddress(Base):
    __tablename__ = "party_address"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    party_id: Mapped[int] = mapped_column(ForeignKey("party.id"), nullable=False)
    address_id: Mapped[int] = mapped_column(ForeignKey("address.id"), nullable=False)
    type: Mapped[Optional[str]] = mapped_column(String(50))

    party: Mapped["Party"] = relationship("Party", back_populates="addresses")
    address: Mapped["Address"] = relationship("Address", back_populates="parties")
