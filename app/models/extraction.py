from pydantic import BaseModel, Field

class Extraction(BaseModel):
    id: int
    reference: str = None
    description: str = None
    meetingId: int 
