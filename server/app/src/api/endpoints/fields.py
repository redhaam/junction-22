from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas
from src.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Field])
def read_fields(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve fields.
    """
    fields = crud.field.get_multi(db, skip=skip, limit=limit)
    
    return fields


@router.post("/", response_model=schemas.Field)
def create_field(
    *,
    db: Session = Depends(deps.get_db),
    field_in: schemas.FieldCreate
) -> Any:
    """
    Create new field.
    """
    field = crud.field.create(db=db, obj_in=field_in)
    
    return field


@router.put("/{id}", response_model=schemas.Field)
def update_lieu(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    field_in: schemas.FieldUpdate
) -> Any:
    """
    Update un field.
    """
    field = crud.field.get(db=db, id=id)
    field = crud.field.update(db=db, db_obj=field, obj_in=field_in)
    
    return field


@router.get("/{id}", response_model=schemas.Field)
def read_field(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Get field by ID.
    """
    field = crud.field.get(db=db, id=id)
    if not field:
        raise HTTPException(status_code=404, detail="Field not found")

    return field


@router.delete("/{id}", response_model=schemas.Field)
def delete_field(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Supprimer un field.
    """
    field = crud.field.get(db=db, id=id)
    if not field:
        raise HTTPException(status_code=404, detail="Field not found")

    field = crud.field.remove(db=db, id=id)
    return field
