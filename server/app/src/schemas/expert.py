from typing import Optional

from pydantic import BaseModel


class ExpertBase(BaseModel):
    attribute: Optional[str] = None



# Properties to receive via API on creation
class ExpertCreate(ExpertBase):
    id: int
    attribute: str


# Properties to receive via API on update
class ExpertUpdate(ExpertBase):
    attribute: Optional[str] = None


class ExpertInDBBase(ExpertBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Expert(ExpertInDBBase):
    pass


# Additional properties stored in DB
class ExpertInDB(ExpertInDBBase):
    pass