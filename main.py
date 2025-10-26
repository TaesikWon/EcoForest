from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routers import eco_router, geo_router

app = FastAPI(title="TerraMap 🌍")

# 정적 파일 연결 (Bootstrap, 이미지 등)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 템플릿 엔진 설정
templates = Jinja2Templates(directory="templates")

# 라우터 등록
app.include_router(eco_router.router)
app.include_router(geo_router.router)

# 홈 페이지
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "TerraMap 홈"}
    )
