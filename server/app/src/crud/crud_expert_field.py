from typing import Any, Dict, List, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import or_
from src.crud.base import CRUDBase
from src.models.expert_field import ExpertField
from src.schemas.expert_field import ExpertFieldCreate, ExpertFieldUpdate
from sqlalchemy.exc import IntegrityError

class CRUDExpertField(CRUDBase[ExpertField, ExpertFieldCreate, ExpertFieldUpdate]):
    def get(self, db: Session, expert_id: int, field_id: int) -> ExpertField:
        return db.query(self.model).filter(self.model.expert_id == expert_id,self.model.field_id == field_id).first()

    def update(
        self,
        db: Session,
        *,
        db_obj: Any,
        obj_in: Union[ExpertFieldUpdate, Dict[str, Any]]
    ) -> ExpertField:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.__dict__
        print(obj_data,update_data)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj 

    def create(
        self, db: Session, *, obj_in: ExpertFieldCreate
    ) -> ExpertField:
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
        #     self.remove(db,expert_id=obj_in_data.get('expert_id'),field_id=obj_in_data.get('field_id'))
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

    def remove(self, db: Session, *, expert_id: int, field_id: int) -> ExpertField:
        obj = db.query(self.model).filter(self.model.expert_id == expert_id,self.model.field_id == field_id).first()
        db.delete(obj)
        db.commit()
        return obj





expert_field = CRUDExpertField(ExpertField)
