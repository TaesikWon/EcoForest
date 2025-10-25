from fastapi import FastAPI
from app.routers import router_forest, router_geo  # ✅ 라우터 불러오기

app = FastAPI()

# ✅ 라우터 등록
app.include_router(router_forest.router)
app.include_router(router_geo.router)

@app.get("/")
def home():
    return {"message": "Welcome to TerraMap 🌍"}
