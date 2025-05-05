from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ingest_and_qa():
    response = client.post("/ingest/", files={"files": ("test.txt", b"Test document content")})
    assert response.status_code == 200

    doc_ids = list(response.json().get("documents", {}).keys())
    if doc_ids:
        qa_response = client.get(f"/qa/?q=What is test&doc_ids={doc_ids[0]}")
        assert qa_response.status_code == 200