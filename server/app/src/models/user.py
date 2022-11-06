from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from src.db.base_class import Base
import enum

class UserType(int,enum.Enum):
    Inventor = 1
    InovationSupport = 2
    Expert = 3
    Foundation = 4


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    # is_superuser = Column(Boolean(), default=False)
    user_type = Column(Enum(UserType),nullable=False, default=1)
    items = relationship("Item", back_populates="owner")
    projects = relationship("Project", back_populates="owner")
    # fields = relationship("Field", back_populates="owner")



