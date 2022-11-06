from typing import Any, Dict, Union

from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models.inventor import Inventor
from src.schemas.inventor import InventorCreate, InventorUpdate


class CRUDInventor(CRUDBase[Inventor, InventorCreate, InventorUpdate]):
    # def get_by_email(self, db: Session, *, email: str) -> Optional[Inventor]:
    #     return db.query(Inventor).filter(Inventor.email == email).first()

    def create(self, db: Session, *, obj_in: InventorCreate) -> Inventor:
        db_obj = Inventor(
            id=obj_in.id,
            status=obj_in.status,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Inventor, obj_in: Union[Inventor, Dict[str, Any]]
    ) -> Inventor:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["status"]:
            d = {}
            d["status"] = update_data["status"]
            update_data = d
        else:
            update_data = {}
        return super().update(db, db_obj=db_obj, obj_in=update_data)




inventor = CRUDInventor(Inventor)
