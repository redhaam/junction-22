from typing import Optional, Tuple

from pydantic import BaseModel


# Shared properties
class FeedbackBase(BaseModel):
    expert_id: Optional[int] = None
    project_id: Optional[int] = None
# Properties to receive on item creation
class FeedbackCreate(FeedbackBase):
    expert_id: int
    project_id: int
    business: float
    feasibility: float
    innovation: float


# Properties to receive on item update
class FeedbackUpdate(FeedbackBase):
    pass


# Properties shared by models stored in DB
class FeedbackInDBBase(FeedbackBase):
    expert_id: int
    project_id: int
    class Config:
        orm_mode = True


# Properties to return to client
class Feedback(FeedbackInDBBase):
    pass


# Properties properties stored in DB
class FeedbackInDB(FeedbackInDBBase):
    pass