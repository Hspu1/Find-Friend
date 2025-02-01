from sqlalchemy import Column, Integer, String

from app.core import Base


class ContactsModel(Base):
    __tablename__ = "contacts"

    contact_id = Column(type_=Integer, primary_key=True, autoincrement=True)

    username = Column(type_=String(20), nullable=False, unique=True)

    telegram = Column(type_=String(50), nullable=True, unique=True, index=True)
    email = Column(type_=String(50), nullable=True, unique=True)
    phone = Column(type_=String(30), nullable=True, unique=True)
    other = Column(type_=String(30), nullable=True, unique=True)
