from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas
from src.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ExpertField])
def read_expert_field(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve expert_fields.
    """
    expert_fields = crud.expert_field.get_multi(db, skip=skip, limit=limit)
    
    return expert_fields


@router.post("/", response_model=schemas.ExpertField)
def create_expert_field(
    *,
    db: Session = Depends(deps.get_db),
    expert_field_in: schemas.ExpertFieldCreate
) -> Any:
    """
    Create new expert_field.
    """
    expert_field = crud.expert_field.create(db=db, obj_in=expert_field_in)
    return expert_field





@router.get("/{expert_id}/{field_id}", response_model=schemas.ExpertField)
def read_expert_field(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int,
    field_id: int
) -> Any:
    """
    Get expert_field by expert_id and field_id.
    """
    expert_field = crud.expert_field.get(db=db, expert_id=expert_id, field_id=field_id)
    if not expert_field:
        raise HTTPException(status_code=404, detail="ExpertField not found")

    return expert_field


@router.delete("/{expert_id}/{field_id}", response_model=schemas.ExpertField)
def delete_expert_field(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int,
    field_id: int

) -> Any:
    """
    Delete an ExpertField.
    """
    expert_field = crud.expert_field.get(db=db, expert_id=expert_id, field_id=field_id)
    if not expert_field:
        raise HTTPException(status_code=404, detail="ExpertField not found")

    expert_field = crud.expert_field.remove(db=db, expert_id=expert_id, field_id=field_id)
    return expert_field

@router.get("/e/{expert_id}/", response_model=List[schemas.ExpertField])
def read_expert_field_by_expert(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int
) -> Any:
    """
    Retrieve ExpertField by expert_id.
    """
    expert_field = crud.expert_field.get_multi_by(db, "expert_id",expert_id)
    
    return expert_field

@router.get("/f/{field_id}/", response_model=List[schemas.ExpertField])
def read_expert_field_by_field(
    *,
    db: Session = Depends(deps.get_db),
    field_id: int
) -> Any:
    """
    Retrieve ExpertField by field_id.
    """
    expert_field = crud.expert_field.get_multi_by(db, "field_id",field_id)
    
    return expert_field