from fastapi import Depends, FastAPI

from .dependencies import get_token_header

from .routers import items

app = FastAPI(dependencies=[])

app.include_router(items.router)
