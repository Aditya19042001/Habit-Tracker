from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    is_active = Column(Boolean, default=True)