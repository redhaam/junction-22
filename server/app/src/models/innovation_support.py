from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, String
from src.db.base_class import Base


class InnovationSupport(Base):
    id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    attribute = Column(String, nullable=True)


