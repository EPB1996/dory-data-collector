import json
from fastapi import APIRouter, HTTPException, status

from app.models.base import Page
from app.models.meeting import Meeting, MeetingRead
from app.models.notionAuth import NotionConfig, NotionTokenRequest, NotionUser
from app.service import firestore
from fastapi.responses import RedirectResponse
from fastapi import Request
import os
import base64
import httpx

from app.core.config import settings


router = APIRouter(
    prefix="/notionAuth",
    tags=["notionAuth"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/config", response_model=NotionConfig)
async def get_config(request: Request) -> NotionConfig:
    """
    Provide OAuth client discovery information.
    """
    print("Config requested")
    config = NotionConfig(
        clientId=settings.OAUTH_CLIENT_ID,
        redirectUri=f"https://{request.url.hostname}/notionAuth/redirect",
        responseType="code",
        usePKCE=True,
        extraParams={
            "owner": "user",
        },
        authorizationEndpoint="https://api.notion.com/v1/oauth/authorize",
        tokenEndpoint=f"https://{request.url.hostname}/notionAuth/token",
    )

    print(config)
    return config


@router.post(
    "/token",
    response_model=NotionUser,
    status_code=status.HTTP_200_OK,
)
async def get_token(codeRequest: NotionTokenRequest, request: Request) -> NotionUser:
    """
    Handle the OAuth authentication process.
    """

    encoded = base64.b64encode(
        f"{settings.OAUTH_CLIENT_ID}:{settings.OAUTH_CLIENT_SECRET}".encode()
    ).decode()

    url = "https://api.notion.com/v1/oauth/token"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Basic {encoded}",
    }
    payload = {
        "grant_type": "authorization_code",
        "code": codeRequest.code,
        "redirect_uri": f"https://{request.url.hostname}/notionAuth/redirect",
    }

    print("Token request payload:", json.dumps(payload))

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, data=json.dumps(payload))
            print(response.text)
            response.raise_for_status()

            data = response.json()

            user = NotionUser(
                access_token=data["access_token"],
                workspace_name=data["workspace_name"],
                workspace_icon=data.get("workspace_icon"),
                name=data["owner"]["user"]["name"],
                user_icon=data["owner"]["user"].get("avatar_url"),
            )
            print("User data:", user)
            return user
        except httpx.HTTPStatusError as e:
            print("HTTP error:", e.response.text)


@router.get("/redirect")
async def oauth_redirect(request: Request):
    """
    Redirect incoming OAuth redirect requests to the custom URL scheme.
    """
    query_params = request.query_params

    app_base_url = settings.DORY_APP_DEEPLINK

    redirect_url = f"{app_base_url}&{query_params}"

    print("URL arguments:", redirect_url)

    return RedirectResponse(url=redirect_url, status_code=301)
