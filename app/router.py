# app/router.py
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.service import analyze_forest_data

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# 🔹 홈 화면: 입력 폼 표시
@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

# 🔹 폼 입력 처리 → 결과 페이지 렌더링
@router.post("/analyze", response_class=HTMLResponse)
async def analyze_forest_form(
    request: Request,
    area1: float = Form(...),
    altitude1: float = Form(...),
    area2: float = Form(...),
    altitude2: float = Form(...),
    area3: float = Form(...),
    altitude3: float = Form(...)
):
    """폼에서 받은 데이터를 분석"""
    data = [
        {"area": area1, "altitude": altitude1},
        {"area": area2, "altitude": altitude2},
        {"area": area3, "altitude": altitude3},
    ]

    result = analyze_forest_data(data)
    return templates.TemplateResponse("result.html", {"request": request, "result": result})
