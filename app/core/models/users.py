from sqlalchemy import (
    Column, Integer, String, DateTime, func
)

from app.core import Base


class UsersModel(Base):
    __tablename__ = "users"

    auth_id = Column(type_=Integer, primary_key=True, autoincrement=True)

    username = Column(type_=String(20), nullable=False, unique=True, index=True)
    age = Column(type_=Integer, nullable=False, index=True)

    hobbies = Column(type_=String(50), nullable=True)
    bio = Column(type_=String(100), nullable=True)

    telegram = Column(type_=String(50), nullable=True, index=True)
    email = Column(type_=String(50), nullable=True)
    phone = Column(type_=String(30), nullable=True)
    other = Column(type_=String(100), nullable=True)

    created_at = Column(
        type_=DateTime(timezone=True), server_default=func.now()
    )
