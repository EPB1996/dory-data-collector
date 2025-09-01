from fastapi import Depends, FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from .dependencies import get_token_header

from .routers import meeting
from .routers import redirect
from .routers import recording
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

app = FastAPI(dependencies=[])

app.include_router(meeting.router)
app.include_router(redirect.router)
app.include_router(recording.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"Validation error: {exc}")
    return PlainTextResponse(str(exc), status_code=400)
