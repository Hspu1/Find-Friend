import os

from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv
from fastapi import APIRouter, Request, HTTPException
from starlette.responses import RedirectResponse

google_auth_router = APIRouter()

fake_firstnames_db = []


load_dotenv()

oauth = OAuth()
oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    },
)


@google_auth_router.get(path="/auth", status_code=200)
async def auth(request: Request):
    try:
        if request.query_params["error"] == "access_denied":
            return RedirectResponse(url="/auth_denied")

    except KeyError:
        token = await oauth.google.authorize_access_token(request)
        user_info = token.get("userinfo")
        request.session['user'] = user_info

        firstname = user_info.get('given_name')
        fake_firstnames_db.append(firstname)

        return RedirectResponse(url='/login_with_name')


@google_auth_router.get(path="/login", status_code=200)
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)
