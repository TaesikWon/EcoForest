# train_ai_models.py
import pandas as pd
from app.service import service_ai

# 🌿 생태 모델 학습
eco_data = pd.DataFrame([
    {"area": 100, "altitude": 200, "eco_score": 0.7},
    {"area": 200, "altitude": 400, "eco_score": 0.9},
    {"area": 50,  "altitude": 150, "eco_score": 0.4},
])
print(service_ai.train_ai_model(eco_data, target_col="eco_score", model_name="eco_model"))

# 🏙️ 도시 모델 학습
geo_data = pd.DataFrame([
    {"population": 500000, "population_density": 15000, "latitude": 37.5, "longitude": 127.0, "urban_score": 0.8},
    {"population": 200000, "population_density": 8000,  "latitude": 35.2, "longitude": 129.1, "urban_score": 0.6},
])
print(service_ai.train_ai_model(geo_data, target_col="urban_score", model_name="geo_model"))
