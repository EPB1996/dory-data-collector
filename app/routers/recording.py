from fastapi import APIRouter
import os
from fastapi import UploadFile, File, HTTPException
from google.cloud import storage


router = APIRouter(
    prefix="/recording",
    tags=["recording"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

# Initialize Google Cloud Storage client
storage_client = storage.Client()
bucket_name = "dory-testing"


@router.post("/upload/")
async def upload_recording(file: UploadFile = File(...)):
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file.filename)
        blob.upload_from_file(file.file, content_type=file.content_type)
        return {"message": f"File {file.filename} uploaded successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")


@router.get("/download/{filename}")
async def download_recording(filename: str):
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(filename)
        if not blob.exists():
            raise HTTPException(status_code=404, detail="File not found.")
        destination_file = os.path.join("/tmp", filename)
        blob.download_to_filename(destination_file)
        return {
            "message": f"File {filename} downloaded successfully to {destination_file}."
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to download file: {str(e)}"
        )
