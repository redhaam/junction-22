from typing import Optional

from pydantic import BaseModel


class InnovationSupportBase(BaseModel):
    attribute: Optional[str] = None



# Properties to receive via API on creation
class InnovationSupportCreate(InnovationSupportBase):
    id: int
    attribute: str


# Properties to receive via API on update
class InnovationSupportUpdate(InnovationSupportBase):
    attribute: Optional[str] = None


class InnovationSupportInDBBase(InnovationSupportBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class InnovationSupport(InnovationSupportInDBBase):
    pass


# Additional properties stored in DB
class InnovationSupportInDB(InnovationSupportInDBBase):
    pass