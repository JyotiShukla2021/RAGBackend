from fastapi import APIRouter, UploadFile, File
from typing import List
import uuid

router = APIRouter()

documents = {}

@router.post("/")
async def ingest_documents(files: List[UploadFile] = File(...)):
    for file in files:
        content = await file.read()
        doc_id = str(uuid.uuid4())
        documents[doc_id] = content.decode()
    return {"status": "success", "count": len(files)}