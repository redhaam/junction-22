from typing import Optional, Tuple

from pydantic import BaseModel


# Shared properties
class ExpertFieldBase(BaseModel):
    expert_id: Optional[int] = None
    field_id: Optional[int] = None
# Properties to receive on item creation
class ExpertFieldCreate(ExpertFieldBase):
    expert_id: int
    field_id: int


# Properties to receive on item update
class ExpertFieldUpdate(ExpertFieldBase):
    pass


# Properties shared by models stored in DB
class ExpertFieldInDBBase(ExpertFieldBase):
    expert_id: int
    field_id: int
    class Config:
        orm_mode = True


# Properties to return to client
class ExpertField(ExpertFieldInDBBase):
    pass


# Properties properties stored in DB
class ExpertFieldInDB(ExpertFieldInDBBase):
    pass