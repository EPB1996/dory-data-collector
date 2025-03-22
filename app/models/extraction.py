from pydantic import BaseModel, Field

class Extraction(BaseModel):
    id: int
    description: str
    startIndex: int
    endIndex: int
    meetingId: int
