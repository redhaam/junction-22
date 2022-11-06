from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, String
from src.models.user import User
from src.db.base_class import Base
from sqlalchemy.orm import relationship

class Inventor(Base):
    id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    status = Column(String, nullable=True)
    
