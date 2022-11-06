from typing import Optional

from pydantic import BaseModel, EmailStr


class InventorBase(BaseModel):
    status: Optional[str] = None



# Properties to receive via API on creation
class InventorCreate(InventorBase):
    id: int
    status: str


# Properties to receive via API on update
class InventorUpdate(InventorBase):
    status: Optional[str] = None


class InventorInDBBase(InventorBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Inventor(InventorInDBBase):
    pass


# Additional properties stored in DB
class InventorInDB(InventorInDBBase):
    pass