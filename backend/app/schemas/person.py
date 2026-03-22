from __future__ import annotations

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PersonBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    birth_date: Optional[date] = None
    username: str
    email: str


class PersonCreate(PersonBase):
    pass


class PersonRead(PersonBase):
    id: int
    type: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
