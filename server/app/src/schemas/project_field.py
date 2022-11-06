from typing import Optional, Tuple

from pydantic import BaseModel


# Shared properties
class ProjectFieldBase(BaseModel):
    project_id: Optional[int] = None
    field_id: Optional[int] = None
# Properties to receive on item creation
class ProjectFieldCreate(ProjectFieldBase):
    project_id: int
    field_id: int


# Properties to receive on item update
class ProjectFieldUpdate(ProjectFieldBase):
    pass


# Properties shared by models stored in DB
class ProjectFieldInDBBase(ProjectFieldBase):
    project_id: int
    field_id: int
    class Config:
        orm_mode = True


# Properties to return to client
class ProjectField(ProjectFieldInDBBase):
    pass


# Properties properties stored in DB
class ProjectFieldInDB(ProjectFieldInDBBase):
    pass