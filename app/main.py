from fastapi import Depends, FastAPI

from .dependencies import get_token_header

from .routers import meeting

app = FastAPI(dependencies=[])

app.include_router(meeting.router)
