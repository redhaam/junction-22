from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas
from src.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ExpertProject])
def read_expert_project(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve expert_projects.
    """
    expert_projects = crud.expert_project.get_multi(db, skip=skip, limit=limit)
    
    return expert_projects


@router.post("/", response_model=schemas.ExpertProject)
def create_expert_project(
    *,
    db: Session = Depends(deps.get_db),
    expert_project_in: schemas.ExpertProjectCreate
) -> Any:
    """
    Create new expert_project.
    """
    expert_project = crud.expert_project.create(db=db, obj_in=expert_project_in)
    return expert_project





@router.get("/{expert_id}/{project_id}", response_model=schemas.ExpertProject)
def read_expert_project(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int,
    project_id: int
) -> Any:
    """
    Get expert_project by expert_id and project_id.
    """
    expert_project = crud.expert_project.get(db=db, expert_id=expert_id, project_id=project_id)
    if not expert_project:
        raise HTTPException(status_code=404, detail="ExpertProject not found")

    return expert_project


@router.delete("/{expert_id}/{project_id}", response_model=schemas.ExpertProject)
def delete_expert_project(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int,
    project_id: int

) -> Any:
    """
    Delete an ExpertProject.
    """
    expert_project = crud.expert_project.get(db=db, expert_id=expert_id, project_id=project_id)
    if not expert_project:
        raise HTTPException(status_code=404, detail="ExpertProject not found")

    expert_project = crud.expert_project.remove(db=db, expert_id=expert_id, project_id=project_id)
    return expert_project

@router.get("/e/{expert_id}/", response_model=List[schemas.ExpertProject])
def read_expert_project_by_expert(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int
) -> Any:
    """
    Retrieve ExpertProject by expert_id.
    """
    expert_project = crud.expert_project.get_multi_by(db, "expert_id",expert_id)
    
    return expert_project

@router.get("/p/{project_id}/", response_model=List[schemas.ExpertProject])
def read_expert_project_by_project(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int
) -> Any:
    """
    Retrieve ExpertProject by project_id.
    """
    expert_project = crud.expert_project.get_multi_by(db, "project_id",project_id)
    
    return expert_project