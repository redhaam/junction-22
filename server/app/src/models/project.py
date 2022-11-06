from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Project(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    document_link = Column(String, nullable=True)
    keyword1 = Column(String, nullable=True)
    keyword2 = Column(String, nullable=True)
    keyword3 = Column(String, nullable=True)
    team_size = Column(Integer, nullable=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="projects")


