from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.api import deps
from src.core.google import upload_file
from fastapi.encoders import jsonable_encoder

router = APIRouter()
bucket_name = 'junction-innov-fi'



@router.get("/", response_model=List[schemas.Project])
def read_projects(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_inventor),
) -> Any:
    """
    Retrieve projects.
    """
    if crud.user.is_superuser(current_user):
        projects = crud.project.get_multi(db,owner_id=current_user.id, skip=skip, limit=limit)
    else:
        projects = crud.project.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return projects


@router.post("/", response_model=schemas.Project)
def create_project(
    *,
    db: Session = Depends(deps.get_db),
    project_in: schemas.ProjectCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new project.
    """

    project = crud.project.create_with_owner(db=db, obj_in=project_in, owner_id=current_user.id)
    return project

@router.post("/{id}", response_model=schemas.Project)
def upload_project_document(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    file: UploadFile= File(default=""),
    current_user: models.User = Depends(deps.get_current_inventor),
) -> Any:
    """
    Upload project document.
    """
    project = crud.project.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not crud.user.is_superuser(current_user) and (project.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    
    if file:
        document_link = upload_file(bucket_name, file, file.filename)
        #print(document_link)
        project_in = {}
        project_in["document_link"] = document_link
        project_in = schemas.ProjectUpdate(**project_in)
        print(project_in)
    
    project = crud.project.update(db=db, db_obj=project, obj_in=project_in)
    
    

    return project

@router.put("/{id}", response_model=schemas.Project)
def update_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    project_in: schemas.ProjectUpdate,
    current_user: models.User = Depends(deps.get_current_inventor),
) -> Any:
    """
    Update an project.
    """
    project = crud.project.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not crud.user.is_superuser(current_user) and (project.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    project = crud.project.update(db=db, db_obj=project, obj_in=project_in)
    return project


@router.get("/{id}", response_model=schemas.Project)
def read_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get project by ID.
    """
    project = crud.project.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not crud.user.is_superuser(current_user) and (project.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    if not (crud.user.is_inventor(current_user) or crud.user.is_expert_affected(db,current_user,id)):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return project


@router.delete("/{id}", response_model=schemas.Project)
def delete_project(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_inventor),
) -> Any:
    """
    Delete an project.
    """
    project = crud.project.get(db=db, id=id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not crud.user.is_superuser(current_user) and (project.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    project = crud.project.remove(db=db, id=id)
    return project
