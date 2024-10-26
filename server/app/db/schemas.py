from sqlalchemy import Column, String, Integer, DateTime, ARRAY
from app.db.dbconnect import Base


class UserSchema(Base):
    __tablename__ = "UserInfo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, nullable=False)


class EventSchema(Base):
    __tablename__ = "EventData"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    organizer = Column(String, nullable=False)
    opentime = Column(DateTime, nullable=False)
    duration = Column(DateTime, nullable=False)
    location = Column(String, nullable=False)
    joiners = Column(ARRAY(String), nullable=False)
