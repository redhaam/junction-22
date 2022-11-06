from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from src import models, schemas
from src.crud import crud_inventor, crud_user
from src.api import deps
from src.core.config import settings
from enum import Enum

router = APIRouter()


@router.get("/", response_model=List[schemas.Inventor])
def read_inventors(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve inventors.
    """
    inventors = crud_inventor.inventor.get_multi(db, skip=skip, limit=limit)
    return inventors



@router.post("/", response_model=schemas.Inventor)
def create_inventor(
    *,
    db: Session = Depends(deps.get_db),
    inventor_in: schemas.InventorCreate,
) -> Any:
    """
    Create new inventor.
    """
    inventor = crud_inventor.inventor.get(db, inventor_in.id)
    if inventor:
        raise HTTPException(
            status_code=400,
            detail="The inventor with this username already exists in the system.",
        )
    is_inventor = crud_user.user.get(db,inventor_in.id).__dict__['user_type'].value
    if is_inventor != 1:
        raise HTTPException(
            status_code=400,
            detail="This user is not an inventor.",
        )

    inventor = crud_inventor.inventor.create(db, obj_in=inventor_in)

    return inventor


@router.get("/{inventor_id}", response_model=schemas.Inventor)
def read_user_by_id(
    inventor_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific inventor by id.
    """
    inventor = crud_inventor.inventor.get(db, id=inventor_id)
    if not inventor:
        raise HTTPException(
            status_code=404,
            detail="The inventor with this username does not exist in the system",
        )
    return inventor


@router.put("/{inventor_id}", response_model=schemas.Inventor)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    inventor_id: int,
    user_in: schemas.UserUpdate,
) -> Any:
    """
    Update a inventor.
    """
    inventor = crud_inventor.inventor.get(db, id=inventor_id)
    if not inventor:
        raise HTTPException(
            status_code=404,
            detail="The inventor with this username does not exist in the system",
        )
    inventor = crud_inventor.inventor.update(db, db_obj=inventor_id, obj_in=user_in)
    return inventor
