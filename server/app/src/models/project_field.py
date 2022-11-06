from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, String
from src.db.base_class import Base
from sqlalchemy.orm import relationship

class ProjectField(Base):
    project = relationship("Project")
    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True)
    field = relationship("Field")
    field_id = Column(Integer, ForeignKey("field.id"), primary_key=True)
    since = Column(String, nullable=True)