from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, String
from src.db.base_class import Base
from sqlalchemy.orm import relationship

class Evaluation(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    expert = relationship("Expert")
    expert_id = Column(Integer, ForeignKey("expert.id"), primary_key=True)
    project = relationship("Project")
    project_id = Column(Integer, ForeignKey("project.id"), primary_key=True)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
