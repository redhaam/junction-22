from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from src import models, schemas
from src.crud import crud_innovation_support, crud_user
from src.api import deps
from src.core.config import settings
from enum import Enum

router = APIRouter()


@router.get("/", response_model=List[schemas.InnovationSupport])
def read_innovation_supports(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve innovation_supports.
    """
    innovation_supports = crud_innovation_support.innovation_support.get_multi(db, skip=skip, limit=limit)
    return innovation_supports



@router.post("/", response_model=schemas.InnovationSupport)
def create_innovation_support(
    *,
    db: Session = Depends(deps.get_db),
    innovation_support_in: schemas.InnovationSupportCreate,
) -> Any:
    """
    Create new innovation_support.
    """
    innovation_support = crud_innovation_support.innovation_support.get(db, innovation_support_in.id)
    if innovation_support:
        raise HTTPException(
            status_code=400,
            detail="The innovation_support with this username already exists in the system.",
        )
    is_innovation_support = crud_user.user.get(db,innovation_support_in.id).__dict__['user_type'].value
    if is_innovation_support != 3:
        raise HTTPException(
            status_code=400,
            detail="This user is not an innovation_support.",
        )

    innovation_support = crud_innovation_support.innovation_support.create(db, obj_in=innovation_support_in)

    return innovation_support


@router.get("/{innovation_support_id}", response_model=schemas.InnovationSupport)
def read_user_by_id(
    innovation_support_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific innovation_support by id.
    """
    innovation_support = crud_innovation_support.innovation_support.get(db, id=innovation_support_id)
    if not innovation_support:
        raise HTTPException(
            status_code=404,
            detail="The innovation_support with this username does not exist in the system",
        )
    return innovation_support


@router.put("/{innovation_support_id}", response_model=schemas.InnovationSupport)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    innovation_support_id: int,
    user_in: schemas.UserUpdate,
) -> Any:
    """
    Update a innovation_support.
    """
    innovation_support = crud_innovation_support.innovation_support.get(db, id=innovation_support_id)
    if not innovation_support:
        raise HTTPException(
            status_code=404,
            detail="The innovation_support with this username does not exist in the system",
        )
    innovation_support = crud_innovation_support.innovation_support.update(db, db_obj=innovation_support_id, obj_in=user_in)
    return innovation_support
