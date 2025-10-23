from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.router import router

app = FastAPI()
app.include_router(router)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "message": "ForestEcoAI is ready!"}
    )
