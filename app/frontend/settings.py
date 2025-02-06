from fastapi import APIRouter
from starlette.responses import HTMLResponse


settings_router = APIRouter()


@settings_router.get("/settings", response_class=HTMLResponse)
def html_landing():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                align-items: flex-start;
                justify-content: center;
                background-image: url('https://github.com/user-attachments/assets/9aec2db1-371c-4c3b-bc95-0bbc8dd1c8bd');
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
            }
    """
