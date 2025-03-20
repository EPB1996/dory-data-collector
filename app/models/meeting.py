
from typing import Optional

from pydantic import BaseModel


class MeetingBase(BaseModel):
    title: str
    description: Optional[str] = None
    metaData: Optional[str] = None
    creationTime: Optional[int] = None
    meetingState: Optional[str] = None
    

class MeetingRead(MeetingBase):
    id: str

    class Config:
        orm_mode = True

class MeetingCreate(MeetingBase):
    pass