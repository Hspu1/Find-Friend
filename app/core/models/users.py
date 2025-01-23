from sqlalchemy import (
    Column, Integer, String, ForeignKey, DateTime, func
)

from app.core import Base


class UsersModel(Base):
    __tablename__ = "users"

    auth_id = Column(type_=Integer, primary_key=True, autoincrement=True)

    username = Column(type_=String(20), nullable=False, unique=True)
    age = Column(type_=Integer, nullable=False)

    hobbies = Column(type_=String(50), nullable=True)
    bio = Column(type_=String(100), nullable=True)
    contact_me = Column(String(20), ForeignKey("contact.username"))

    created_at = Column(
        type_=DateTime(timezone=True), server_default=func.now()
    )
    updated_at = Column(
        type_=DateTime(timezone=True),
        server_default=func.now(), onupdate=func.now()
    )
