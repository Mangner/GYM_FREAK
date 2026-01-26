from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class OrganizationBase(BaseModel):
    name: str
    description: Optional[str] = None


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationRead(OrganizationBase):
    id: int
    type: str
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
