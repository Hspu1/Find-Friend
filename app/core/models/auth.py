from sqlalchemy import Column, Integer, String

from app.core import Base


class AuthModel(Base):
    __tablename__ = "auth"

    auth_id = Column(type_=Integer, primary_key=True, autoincrement=True)

    username = Column(type_=String(20), nullable=False, unique=True)
    hashed_psw = Column(type=String(100), nullable=False, unique=True)
