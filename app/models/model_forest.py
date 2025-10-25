# app/models/model_forest.py
from pydantic import BaseModel, Field


class ForestRegion(BaseModel):
    """
    산림 분석용 데이터 모델
    - name: 지역 이름
    - area: 면적(ha)
    - altitude: 평균 고도(m)
    """
    name: str = Field(..., description="지역 이름")
    area: float = Field(gt=0, description="면적(ha)")
    altitude: float = Field(..., description="평균 고도(m)")
