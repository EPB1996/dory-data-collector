import datetime
from typing import Optional
from pydantic import BaseModel
from app.models.extraction import Extraction
from app.models.task import Task


class Meeting(BaseModel):
    randomIdentifier: str

    dory_id: str
    title: str
    text: Optional[str] = None
    metaData: Optional[dict] = None
    creationTime: Optional[datetime.datetime] = None
    meetingState: Optional[str] = None

    extractions: Optional[list[Extraction]] = []
    tasks: Optional[list[Task]] = []

    user: Optional[str] = None
    


class MeetingRead(Meeting):
    id: str
