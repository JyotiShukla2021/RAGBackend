from fastapi import APIRouter, Query
from typing import List
from app.ingestion import documents
import random

router = APIRouter()

@router.get("/")
async def ask_question(q: str, doc_ids: List[str] = Query(default=[])):
    selected_docs = [documents[doc_id] for doc_id in doc_ids if doc_id in documents]
    answer = f"Answer based on {len(selected_docs)} documents: {q} -> {random.choice(selected_docs) if selected_docs else 'No relevant content'}"
    return {"question": q, "answer": answer}