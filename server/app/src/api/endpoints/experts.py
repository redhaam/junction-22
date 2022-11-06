from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from src import models, schemas
from src.crud import crud_expert, crud_user
from src.api import deps
from src.core.config import settings
from enum import Enum

router = APIRouter()


@router.get("/", response_model=List[schemas.Expert])
def read_experts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve experts.
    """
    experts = crud_expert.expert.get_multi(db, skip=skip, limit=limit)
    return experts



@router.post("/", response_model=schemas.Expert)
def create_expert(
    *,
    db: Session = Depends(deps.get_db),
    expert_in: schemas.ExpertCreate,
) -> Any:
    """
    Create new expert.
    """
    expert = crud_expert.expert.get(db, expert_in.id)
    if expert:
        raise HTTPException(
            status_code=400,
            detail="The expert with this username already exists in the system.",
        )
    is_expert = crud_user.user.get(db,expert_in.id).__dict__['user_type'].value
    if is_expert != 3:
        raise HTTPException(
            status_code=400,
            detail="This user is not an expert.",
        )

    expert = crud_expert.expert.create(db, obj_in=expert_in)

    return expert


@router.get("/{expert_id}", response_model=schemas.Expert)
def read_user_by_id(
    expert_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific expert by id.
    """
    expert = crud_expert.expert.get(db, id=expert_id)
    if not expert:
        raise HTTPException(
            status_code=404,
            detail="The expert with this username does not exist in the system",
        )
    return expert


@router.put("/{expert_id}", response_model=schemas.Expert)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    expert_id: int,
    user_in: schemas.UserUpdate,
) -> Any:
    """
    Update a expert.
    """
    expert = crud_expert.expert.get(db, id=expert_id)
    if not expert:
        raise HTTPException(
            status_code=404,
            detail="The expert with this username does not exist in the system",
        )
    expert = crud_expert.expert.update(db, db_obj=expert_id, obj_in=user_in)
    return expert
