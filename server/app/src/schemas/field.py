from typing import Optional

from pydantic import BaseModel


# Shared properties
class FieldBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class FieldCreate(FieldBase):
    title: str


# Properties to receive on item update
class FieldUpdate(FieldBase):
    pass


# Properties shared by models stored in DB
class FieldInDBBase(FieldBase):
    id: int
    title: str

    class Config:
        orm_mode = True


# Properties to return to client
class Field(FieldInDBBase):
    pass


# Properties properties stored in DB
class FieldInDB(FieldInDBBase):
    pass
