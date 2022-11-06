from typing import Any, Dict, Union

from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models.expert import Expert
from src.schemas.expert import ExpertCreate, ExpertUpdate


class CRUDExpert(CRUDBase[Expert, ExpertCreate, ExpertUpdate]):

    def create(self, db: Session, *, obj_in: ExpertCreate) -> Expert:
        db_obj = Expert(
            id=obj_in.id,
            attribute=obj_in.attribute,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Expert, obj_in: Union[Expert, Dict[str, Any]]
    ) -> Expert:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["attribute"]:
            d = {}
            d["attribute"] = update_data["attribute"]
            update_data = d
        else:
            update_data = {}
        return super().update(db, db_obj=db_obj, obj_in=update_data)




expert = CRUDExpert(Expert)
