from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from src import models, schemas
from src.crud import crud_foundation_admin, crud_user
from src.api import deps
from src.core.config import settings
from enum import Enum

router = APIRouter()


@router.get("/", response_model=List[schemas.FoundationAdmin])
def read_foundation_admins(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve foundation_admins.
    """
    foundation_admins = crud_foundation_admin.foundation_admin.get_multi(db, skip=skip, limit=limit)
    return foundation_admins



@router.post("/", response_model=schemas.FoundationAdmin)
def create_foundation_admin(
    *,
    db: Session = Depends(deps.get_db),
    foundation_admin_in: schemas.FoundationAdminCreate,
) -> Any:
    """
    Create new foundation_admin.
    """
    foundation_admin = crud_foundation_admin.foundation_admin.get(db, foundation_admin_in.id)
    if foundation_admin:
        raise HTTPException(
            status_code=400,
            detail="The foundation_admin with this username already exists in the system.",
        )
    is_foundation_admin = crud_user.user.get(db,foundation_admin_in.id).__dict__['user_type'].value
    if is_foundation_admin != 2:
        raise HTTPException(
            status_code=400,
            detail="This user is not an foundation_admin.",
        )

    foundation_admin = crud_foundation_admin.foundation_admin.create(db, obj_in=foundation_admin_in)

    return foundation_admin


@router.get("/{foundation_admin_id}", response_model=schemas.FoundationAdmin)
def read_user_by_id(
    foundation_admin_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific foundation_admin by id.
    """
    foundation_admin = crud_foundation_admin.foundation_admin.get(db, id=foundation_admin_id)
    if not foundation_admin:
        raise HTTPException(
            status_code=404,
            detail="The foundation_admin with this username does not exist in the system",
        )
    return foundation_admin


@router.put("/{foundation_admin_id}", response_model=schemas.FoundationAdmin)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    foundation_admin_id: int,
    user_in: schemas.UserUpdate,
) -> Any:
    """
    Update a foundation_admin.
    """
    foundation_admin = crud_foundation_admin.foundation_admin.get(db, id=foundation_admin_id)
    if not foundation_admin:
        raise HTTPException(
            status_code=404,
            detail="The foundation_admin with this username does not exist in the system",
        )
    foundation_admin = crud_foundation_admin.foundation_admin.update(db, db_obj=foundation_admin_id, obj_in=user_in)
    return foundation_admin
