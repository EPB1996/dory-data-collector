from typing import Optional
from pydantic import BaseModel


class NotionUser(BaseModel):
    access_token: str
    workspace_name: str
    workspace_icon: Optional[str]
    name: str
    user_icon: Optional[str]


class NotionConfig(BaseModel):
    clientId: str
    redirectUri: str
    responseType: str
    usePKCE: bool
    extraParams: dict
    authorizationEndpoint: str
    tokenEndpoint: str


class NotionTokenRequest(BaseModel):
    code: str
