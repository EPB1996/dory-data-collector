import datetime
from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    description: str = None
    reference: str = None
    data: str = None
    creationTime: Optional[datetime.datetime] = None
    taskState: str = None
    extractionId: int = None
    meetingId: int = None


test:Task = {
    "id": 1,
    "description": "Task 1",
    "reference": "Reference 1",
    "data": "Data 1",
    "creationTime": 1,
    "taskState": "State 1",
    "extractionId": 1
}