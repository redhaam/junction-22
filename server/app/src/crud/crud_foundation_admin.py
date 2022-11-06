from typing import Any, Dict, Union

from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models.foundation_admin import FoundationAdmin
from src.schemas.foundation_admin import FoundationAdminCreate, FoundationAdminUpdate


class CRUDFoundationAdmin(CRUDBase[FoundationAdmin, FoundationAdminCreate, FoundationAdminUpdate]):

    def create(self, db: Session, *, obj_in: FoundationAdminCreate) -> FoundationAdmin:
        db_obj = FoundationAdmin(
            id=obj_in.id,
            attribute=obj_in.attribute,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: FoundationAdmin, obj_in: Union[FoundationAdmin, Dict[str, Any]]
    ) -> FoundationAdmin:
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




foundation_admin = CRUDFoundationAdmin(FoundationAdmin)
