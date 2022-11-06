from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas
from src.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ProjectField])
def read_project_field(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve project_fields.
    """
    project_fields = crud.project_field.get_multi(db, skip=skip, limit=limit)
    
    return project_fields


@router.post("/", response_model=schemas.ProjectField)
def create_project_field(
    *,
    db: Session = Depends(deps.get_db),
    project_field_in: schemas.ProjectFieldCreate
) -> Any:
    """
    Create new project_field.
    """
    project_field = crud.project_field.create(db=db, obj_in=project_field_in)
    return project_field





@router.get("/{project_id}/{field_id}", response_model=schemas.ProjectField)
def read_project_field(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int,
    field_id: int
) -> Any:
    """
    Get project_field by project_id and field_id.
    """
    project_field = crud.project_field.get(db=db, project_id=project_id, field_id=field_id)
    if not project_field:
        raise HTTPException(status_code=404, detail="ProjectField not found")

    return project_field


@router.delete("/{project_id}/{field_id}", response_model=schemas.ProjectField)
def delete_project_field(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int,
    field_id: int

) -> Any:
    """
    Delete an ProjectField.
    """
    project_field = crud.project_field.get(db=db, project_id=project_id, field_id=field_id)
    if not project_field:
        raise HTTPException(status_code=404, detail="ProjectField not found")

    project_field = crud.project_field.remove(db=db, project_id=project_id, field_id=field_id)
    return project_field

@router.get("/p/{project_id}/", response_model=List[schemas.ProjectField])
def read_project_field_by_project(
    *,
    db: Session = Depends(deps.get_db),
    project_id: int
) -> Any:
    """
    Retrieve ProjectField by project_id.
    """
    project_field = crud.project_field.get_multi_by(db, "project_id",project_id)
    
    return project_field

@router.get("/f/{field_id}/", response_model=List[schemas.ProjectField])
def read_project_field_by_field(
    *,
    db: Session = Depends(deps.get_db),
    field_id: int
) -> Any:
    """
    Retrieve ProjectField by field_id.
    """
    project_field = crud.project_field.get_multi_by(db, "field_id",field_id)
    
    return project_field