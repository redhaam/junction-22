from typing import Any, Dict, Union

from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models.innovation_support import InnovationSupport
from src.schemas.innovation_support import InnovationSupportCreate, InnovationSupportUpdate


class CRUDInnovationSupport(CRUDBase[InnovationSupport, InnovationSupportCreate, InnovationSupportUpdate]):

    def create(self, db: Session, *, obj_in: InnovationSupportCreate) -> InnovationSupport:
        db_obj = InnovationSupport(
            id=obj_in.id,
            attribute=obj_in.attribute,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: InnovationSupport, obj_in: Union[InnovationSupport, Dict[str, Any]]
    ) -> InnovationSupport:
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




innovation_support = CRUDInnovationSupport(InnovationSupport)
