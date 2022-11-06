from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, String, Float
from src.db.base_class import Base
from sqlalchemy.orm import relationship

class Feedback(Base):
    expert = relationship("Expert")
    expert_id = Column(Integer, ForeignKey("expert.id"), primary_key=True)
    project = relationship("Project")
    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True)
    feasibility = Column(Float, nullable=True)
    business = Column(Float, nullable=True)
    innovation = Column(Float, nullable=True)
