__all__ = (
    "homepage_router",
    "login_with_name_router",
    "auth_denied_router",
    "change_name_router",
    "submit_name_router",
    "password_entering_router",
    "questionnaire_router"
)

from .homepage import homepage_router
from .login_with_name import login_with_name_router
from .auth_denied import auth_denied_router
from .change_name import change_name_router
from .submit_name import submit_name_router
from .password_entering import password_entering_router
from .questionnaire import questionnaire_router
