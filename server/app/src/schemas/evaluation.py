from typing import Optional, Tuple

from pydantic import BaseModel


# Shared properties
class EvaluationBase(BaseModel):
    expert_id: Optional[int] = None
    project_id: Optional[int] = None
    title: Optional[str] = None
# Properties to receive on item creation
class EvaluationCreate(EvaluationBase):
    expert_id: int
    project_id: int
    title: str
    description: str


# Properties to receive on item update
class EvaluationUpdate(EvaluationBase):
    pass


# Properties shared by models stored in DB
class EvaluationInDBBase(EvaluationBase):
    title: str
    expert_id: int
    project_id: int
    class Config:
        orm_mode = True


# Properties to return to client
class Evaluation(EvaluationInDBBase):
    pass


# Properties properties stored in DB
class EvaluationInDB(EvaluationInDBBase):
    pass