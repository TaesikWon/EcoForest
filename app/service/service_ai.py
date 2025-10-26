# app/service/service_ai.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os

MODEL_PATH = "app/service/models"
os.makedirs(MODEL_PATH, exist_ok=True)


def train_ai_model(data: pd.DataFrame, target_col: str, model_name: str):
    """
    ✅ AI 예측 모델 학습 및 저장
    """
    X = data.drop(columns=[target_col])
    y = data[target_col]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LinearRegression()
    model.fit(X_scaled, y)

    # 모델 저장
    joblib.dump((model, scaler), os.path.join(MODEL_PATH, f"{model_name}.pkl"))
    return f"{model_name} 모델이 학습 및 저장되었습니다."


def predict_ai_score(data: dict, model_name: str):
    """
    ✅ 입력 데이터 기반 예측값 반환
    """
    model_file = os.path.join(MODEL_PATH, f"{model_name}.pkl")
    if not os.path.exists(model_file):
        raise FileNotFoundError(f"{model_name}.pkl 모델이 존재하지 않습니다. 먼저 학습을 수행하세요.")

    model, scaler = joblib.load(model_file)
    df = pd.DataFrame([data])
    X_scaled = scaler.transform(df)
    prediction = model.predict(X_scaled)
    return float(prediction[0])
