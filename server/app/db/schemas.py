from sqlalchemy import Column, String, Integer
from app.db.dbconnect import Base


class UserSchema(Base):
    __tablename__ = "UserInfo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, nullable=False)
