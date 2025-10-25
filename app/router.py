from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from .service import analyze_forest_data
from .model import ForestData
from .db import init_db, save_analysis, get_all_history

router = APIRouter()
templates = Jinja2Templates(directory="templates")

init_db()

@router.get("/")
def show_form(request: Request):
    return templates.TemplateResponse(request, "form.html", {"request": request})

@router.post("/analyze")
async def analyze(request: Request):
    form = await request.form()
    try:
        regions = [
            {"name": "1", "area": float(form["area1"]), "altitude": float(form["altitude1"])},
            {"name": "2", "area": float(form["area2"]), "altitude": float(form["altitude2"])},
            {"name": "3", "area": float(form["area3"]), "altitude": float(form["altitude3"])},
        ]
        validated = ForestData(regions=regions)
        result = analyze_forest_data(validated.model_dump())

        save_analysis(result) 

        return templates.TemplateResponse(request, "result.html", {"request": request, "result": result})

    except ValidationError as ve:
        return templates.TemplateResponse(request, "error.html", {"request": request, "message": f"입력 오류: {ve}"})
    except Exception as e:
        return templates.TemplateResponse(request, "error.html", {"request": request, "message": f"처리 오류: {e}"})

@router.get("/history")
def history(request: Request):
    data = get_all_history()
    return templates.TemplateResponse(request, "history.html", {"request": request, "data": data})
