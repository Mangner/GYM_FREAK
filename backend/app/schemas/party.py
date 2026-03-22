from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PartyBase(BaseModel):
    pass


class PartyRead(PartyBase):
    id: int
    type: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
