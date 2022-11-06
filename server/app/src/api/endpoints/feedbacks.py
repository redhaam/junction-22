from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas, models
from src.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Feedback])
def read_feedbacks(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve feedbacks.
    """
    feedbacks = crud.feedback.get_multi(db, skip=skip, limit=limit)
    
    return feedbacks


@router.post("/", response_model=schemas.Feedback)
def create_feedback(
    *,
    db: Session = Depends(deps.get_db),
    feedback_in: schemas.FeedbackCreate,
    current_user: models.User = Depends(deps.get_current_expert),
) -> Any:
    """
    Create new feedback.
    """
    feedback = crud.feedback.create(db=db, obj_in=feedback_in)
    return feedback





@router.get("/{expert_id}/{project_id}", response_model=schemas.Feedback)
def read_feedback(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int,
    project_id: int
) -> Any:
    """
    Get feedback by expert_id and project_id.
    """
    feedback = crud.feedback.get(db=db, expert_id=expert_id, project_id=project_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")

    return feedback


@router.delete("/{expert_id}/{project_id}", response_model=schemas.Feedback)
def delete_feedback(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int,
    project_id: int

) -> Any:
    """
    Delete an Feedback.
    """
    feedback = crud.feedback.get(db=db, expert_id=expert_id, project_id=project_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")

    feedback = crud.feedback.remove(db=db, expert_id=expert_id, project_id=project_id)
    return feedback

@router.get("/e/{expert_id}/", response_model=List[schemas.Feedback])
def read_feedback_by_expert(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int
) -> Any:
    """
    Retrieve Feedback by expert_id.
    """
    feedback = crud.feedback.get_multi_by(db, "expert_id",expert_id)
    
    return feedback

@router.get("/f/{project_id}/", response_model=List[schemas.Feedback])
def read_feedback_by_project(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int
) -> Any:
    """
    Retrieve Feedback by project_id.
    """
    feedback = crud.feedback.get_multi_by(db, "project_id",project_id)
    
    return feedback