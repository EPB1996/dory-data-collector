from typing import Optional
from pydantic import BaseModel
from app.models.extraction import Extraction
from app.models.task import Task


class Meeting(BaseModel):
    dory_id: str
    title: str
    description: Optional[str] = None
    metaData: Optional[str] = None
    creationTime: Optional[int] = None
    meetingState: Optional[str] = None

    extractions: Optional[list[Extraction]] = []
    tasks: Optional[list[Task]] = []

    user: Optional[str] = None


class MeetingRead(Meeting):
    id: str
