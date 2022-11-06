from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas, models
from src.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Evaluation])
def read_evaluations(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve evaluations.
    """
    evaluations = crud.evaluation.get_multi(db, skip=skip, limit=limit)
    
    return evaluations


@router.post("/", response_model=schemas.Evaluation)
def create_evaluation(
    *,
    db: Session = Depends(deps.get_db),
    evaluation_in: schemas.EvaluationCreate,
    current_user: models.User = Depends(deps.get_current_expert),
) -> Any:
    """
    Create new evaluation.
    """
    evaluation = crud.evaluation.create(db=db, obj_in=evaluation_in)
    return evaluation





@router.get("/{expert_id}/{project_id}", response_model=schemas.Evaluation)
def read_evaluation(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int,
    project_id: int
) -> Any:
    """
    Get evaluation by id and expert_id and project_id.
    """
    evaluation = crud.evaluation.get(db=db, expert_id=expert_id, project_id=project_id)
    if not evaluation:
        raise HTTPException(status_code=404, detail="Evaluation not found")

    return evaluation


@router.delete("/{expert_id}/{project_id}", response_model=schemas.Evaluation)
def delete_evaluation(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int,
    project_id: int

) -> Any:
    """
    Delete an Evaluation.
    """
    evaluation = crud.evaluation.get(db=db, id=id, expert_id=expert_id, project_id=project_id)
    if not evaluation:
        raise HTTPException(status_code=404, detail="Evaluation not found")

    evaluation = crud.evaluation.remove(db=db, id=id, expert_id=expert_id, project_id=project_id)
    return evaluation

@router.get("/e/{expert_id}/", response_model=List[schemas.Evaluation])
def read_evaluation_by_expert(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int
) -> Any:
    """
    Retrieve Evaluation by expert_id.
    """
    evaluation = crud.evaluation.get_multi_by(db, "expert_id",expert_id)
    
    return evaluation

@router.get("/p/{project_id}/", response_model=List[schemas.Evaluation])
def read_evaluation_by_project(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int
) -> Any:
    """
    Retrieve Evaluation by project_id.
    """
    evaluation = crud.evaluation.get_multi_by(db, "project_id",project_id)
    
    return evaluation