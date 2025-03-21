from pydantic import BaseModel, Field

class Extraction(BaseModel):
    id: str
    description: str
    startIndex: int
    endIndex: int
