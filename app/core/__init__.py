__all__ = (
    "db_url",
    "async_session_maker",
    "Base",

    "ContactsModel",
    "UsersModel"
)

from .config import db_url, async_session_maker, Base
from .models import ContactsModel, UsersModel
