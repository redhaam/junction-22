from typing import Optional

from pydantic import BaseModel


# Shared properties
class ProjectBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    document_link: Optional[str] = None

# Properties to receive on item creation
class ProjectCreate(ProjectBase):
    title: str
    description: str
    keyword1: str
    keyword2: str
    keyword3: str
    team_size: int
    # document_size: str


# Properties to receive on item update
class ProjectUpdate(ProjectBase):
    document_link: str


# Properties shared by models stored in DB
class ProjectInDBBase(ProjectBase):
    id: int
    title: str
    owner_id: int
    description: str
    keyword1: str
    keyword2: str
    keyword3: str
    team_size: int
    document_size: Optional[str] = None
    class Config:
        orm_mode = True


# Properties to return to client
class Project(ProjectInDBBase):
    pass


# Properties properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass
