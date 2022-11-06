from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from src.core.security import get_password_hash, verify_password
from src.crud.base import CRUDBase
from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate
from .crud_expert_project import expert_project

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            user_type=obj_in.user_type,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data.get("password", None):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_expert_affected(self, db:Session, user: User, project_id: int) -> bool:
        expert_project_obj = expert_project.get(db=db,expert_id=user.id, project_id=project_id)
        if expert_project_obj:
            return True
        else:
            return False

    def is_active(self, user: User) -> bool:
        return user.is_active
    
    def is_inventor(self, user: User) -> bool:
        return self.is_superuser(user) or user.user_type == 1

    def is_expert(self, user: User) -> bool:
        return user.user_type == 3
    
    def is_superuser(self, user: User) -> bool:
        return user.user_type == 4


user = CRUDUser(User);print("created")
