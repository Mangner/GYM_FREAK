from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PartyRoleBase(BaseModel):
    type: str
    active_from: Optional[date] = None
    active_to: Optional[date] = None


class PartyRoleCreate(PartyRoleBase):
    pass


class PartyRoleRead(PartyRoleBase):
    id: int
    party_id: int

    model_config = ConfigDict(from_attributes=True)
