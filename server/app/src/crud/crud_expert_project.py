from typing import Any, Dict, List, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import or_
from src.crud.base import CRUDBase
from src.models.expert_project import ExpertProject
from src.schemas.expert_project import ExpertProjectCreate, ExpertProjectUpdate
from sqlalchemy.exc import IntegrityError

class CRUDExpertProject(CRUDBase[ExpertProject, ExpertProjectCreate, ExpertProjectUpdate]):
    def get(self, db: Session, expert_id: int, project_id: int) -> ExpertProject:
        return db.query(self.model).filter(self.model.expert_id == expert_id,self.model.project_id == project_id).first()

    def update(
        self,
        db: Session,
        *,
        db_obj: Any,
        obj_in: Union[ExpertProjectUpdate, Dict[str, Any]]
    ) -> ExpertProject:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.__dict__
        print(obj_data,update_data)
        for project in obj_data:
            if project in update_data:
                setattr(db_obj, project, update_data[project])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj 

    def create(
        self, db: Session, *, obj_in: ExpertProjectCreate
    ) -> ExpertProject:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        
        # try:
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        # except IntegrityError :
        #     db.rollback()
        #     # obj = db.query(self.model).filter(self.model.user_id == obj_in_data.get('user_id'),self.model.lieu_id == obj_in_data.get('lieu_id')).first()
        #     # db.delete(obj)
        #     # db.commit()
        #     self.remove(db,expert_id=obj_in_data.get('expert_id'),project_id=obj_in_data.get('project_id'))
        #     db.rollback()
        #     db.add(db_obj)
        #     db.commit()
        #     db.refresh(db_obj)

        
        return db_obj

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List:
        result = (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return result

    def get_multi_by(
        self, db: Session, filter_name: str,filter_value: Any
    ) -> List:
        return db.query(self.model).filter(getattr(self.model,filter_name) == filter_value).all()

    def remove(self, db: Session, *, expert_id: int, project_id: int) -> ExpertProject:
        obj = db.query(self.model).filter(self.model.expert_id == expert_id,self.model.project_id == project_id).first()
        db.delete(obj)
        db.commit()
        return obj





expert_project = CRUDExpertProject(ExpertProject)
