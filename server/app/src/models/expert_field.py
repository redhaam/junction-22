from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, String
from src.db.base_class import Base
from sqlalchemy.orm import relationship

class ExpertField(Base):
    expert = relationship("Expert")
    expert_id = Column(Integer, ForeignKey("expert.id"), primary_key=True)
    field = relationship("Field")
    field_id = Column(Integer, ForeignKey("field.id"), primary_key=True)
    since = Column(String, nullable=True)