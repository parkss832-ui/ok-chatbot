from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DocRequest(BaseModel):
    doc_number: str
    issue_date: str

@app.get("/")
def home():
    return {"message": "주민등록 원초본 진위확인 API 서버 정상 동작 중"}

@app.post("/api/check")
async def check_doc(data: DocRequest):
    if data.doc_number == "1245-4555-1511-3536":
        return {"status": "valid", "message": "✅ 유효한 주민등록 원초본입니다"}
    else:
        return {"status": "invalid", "message": "❌ 존재하지 않는 발급번호입니다"}
