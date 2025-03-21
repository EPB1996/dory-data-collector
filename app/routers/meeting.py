from fastapi import APIRouter, HTTPException, status

from app.models.base import Page
from app.models.meeting import Meeting, MeetingRead
from app.service import firestore

MEETING_COLLECTION = "dory-meeting"

router = APIRouter(
    prefix="/meeting",
    tags=["meeting"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get(
    "",
    response_model=Page[MeetingRead],
    status_code=status.HTTP_200_OK,
)
def get_meetings() -> Page[MeetingRead]:
    
    meetings = firestore.get_all_documents(MEETING_COLLECTION)
    return Page(items=meetings, total=len(meetings))


@router.get("/{meeting_id}", response_model=MeetingRead, status_code=status.HTTP_200_OK)
async def read_item(meeting_id: str) -> MeetingRead:
    meeting = firestore.get_document(MEETING_COLLECTION, meeting_id)
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return meeting
    

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MeetingRead)
async def create_meeting(meeting: Meeting) -> MeetingRead:
    existing_meeting = firestore.get_document_by_field(MEETING_COLLECTION, "dory_id", meeting.dory_id)
    existing_meeting_id = MeetingRead(**existing_meeting).id if existing_meeting else None

    if not existing_meeting_id:
        update_time, doc_ref = firestore.add_document(MEETING_COLLECTION, meeting.model_dump())
        meeting = doc_ref.get().to_dict()
        meeting["id"] = doc_ref.id
    else:
        firestore.update_document(MEETING_COLLECTION, existing_meeting_id, meeting.model_dump())
        meeting = meeting.model_dump()
        meeting["id"] = existing_meeting_id

    return meeting


    