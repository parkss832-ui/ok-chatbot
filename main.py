from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 요청 데이터 구조 정의
class DocRequest(BaseModel):
    doc_number: str
    issue_date: str

# ✅ 여러 개 유효 발급번호 + 발급일자 등록
valid_docs = [
    {"doc_number": "1245-4555-1511-3536", "issue_date": "20250916"},
    {"doc_number": "1758-0103-0671-4375", "issue_date": "20250916"},
    {"doc_number": "9999-8888-7777-6666", "issue_date": "20250917"}
]

@app.get("/")
def home():
    return {"message": "주민등록 원초본 진위확인 API 서버 정상 동작 중"}

@app.post("/api/check")
async def check_doc(data: DocRequest):
    # 등록된 발급번호/발급일자 중 하나라도 일치하면 valid 반환
    for doc in valid_docs:
        if data.doc_number == doc["doc_number"] and data.issue_date == doc["issue_date"]:
            return {
                "status": "valid",
                "message": "✅ 유효한 주민등록 원초본입니다"
            }
    return {
        "status": "invalid",
        "message": "✘ 존재하지 않는 발급번호입니다"
    }
