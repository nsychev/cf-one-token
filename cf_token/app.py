from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Header, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# The proxy in front of this app injects the authenticated user's identity as a
# JWT in this header. We echo it back so the user can copy it into their own
# requests as the `cf-access-token` header.
PROXY_HEADER = "cf-access-jwt-assertion"
API_HEADER = "cf-access-token"

_BASE_DIR = Path(__file__).parent
templates = Jinja2Templates(directory=_BASE_DIR / "templates")

app = FastAPI(
    title="CF Access Token",
    version="1",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)
app.mount("/static", StaticFiles(directory=_BASE_DIR / "static"), name="static")


@app.get("/", response_class=HTMLResponse)
def index(
    request: Request,
    token: Annotated[str | None, Header(alias=PROXY_HEADER)] = None,
) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "index.html",
        {"token": token, "api_header": API_HEADER},
    )
