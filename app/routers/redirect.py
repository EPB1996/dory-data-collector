from fastapi import APIRouter, HTTPException, status

from app.models.base import Page
from app.models.meeting import Meeting, MeetingRead
from app.service import firestore
from fastapi.responses import RedirectResponse
from fastapi import Request

router = APIRouter(
    prefix="/redirect",
    tags=["oauth_redirect"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def oauth_redirect(): 
    """
    Redirect incoming OAuth redirect requests to the custom URL scheme.
    """

    print("redirecting to myapp://")
    return RedirectResponse(url="myapp://")



    