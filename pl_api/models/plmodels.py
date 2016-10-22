from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey
)

from .meta import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(Text, unique=True)

class Activity(Base):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    activity_name = Column(Text, nullable=False)
    created_on = Column(DateTime, nullable=False)

class ActivityLog(Base):
    __tablename__ = 'activity_log'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    activity_id = Column(Integer, ForeignKey(Activity.id))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
