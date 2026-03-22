from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict


class AddressBase(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None


class AddressCreate(AddressBase):
    pass


class AddressRead(AddressBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
