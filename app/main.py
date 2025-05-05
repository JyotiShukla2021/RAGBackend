from fastapi import FastAPI
from app.ingestion import router as ingestion_router
from app.retrieval import router as retrieval_router

app = FastAPI(title="RAG Document Q&A System")

app.include_router(ingestion_router, prefix="/ingest")
app.include_router(retrieval_router, prefix="/qa")