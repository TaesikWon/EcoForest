# main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import eco_router, geo_router, rag_router

# ✅ FastAPI 앱 생성
app = FastAPI(title="TerraMap 🌍 AI Platform")

# ✅ 정적 파일 연결 (Bootstrap, 이미지 등)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ 템플릿 엔진 설정
templates = Jinja2Templates(directory="templates")

# ✅ 라우터 등록
app.include_router(eco_router.router)
app.include_router(geo_router.router)
app.include_router(rag_router.router)

# ✅ 홈 페이지
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "TerraMap 홈"}
    )

# ✅ 직접 실행용
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
