from typing import Optional, Tuple

from pydantic import BaseModel


# Shared properties
class ExpertProjectBase(BaseModel):
    expert_id: Optional[int] = None
    project_id: Optional[int] = None
# Properties to receive on item creation
class ExpertProjectCreate(ExpertProjectBase):
    expert_id: int
    project_id: int


# Properties to receive on item update
class ExpertProjectUpdate(ExpertProjectBase):
    pass


# Properties shared by models stored in DB
class ExpertProjectInDBBase(ExpertProjectBase):
    expert_id: int
    project_id: int
    class Config:
        orm_mode = True


# Properties to return to client
class ExpertProject(ExpertProjectInDBBase):
    pass


# Properties properties stored in DB
class ExpertProjectInDB(ExpertProjectInDBBase):
    pass