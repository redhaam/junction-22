from typing import Optional

from pydantic import BaseModel


class FoundationAdminBase(BaseModel):
    attribute: Optional[str] = None



# Properties to receive via API on creation
class FoundationAdminCreate(FoundationAdminBase):
    id: int
    attribute: str


# Properties to receive via API on update
class FoundationAdminUpdate(FoundationAdminBase):
    attribute: Optional[str] = None


class FoundationAdminInDBBase(FoundationAdminBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class FoundationAdmin(FoundationAdminInDBBase):
    pass


# Additional properties stored in DB
class FoundationAdminInDB(FoundationAdminInDBBase):
    pass