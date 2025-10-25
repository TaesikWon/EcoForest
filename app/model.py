# app/model.py
from pydantic import BaseModel, Field
from typing import List

# 🌲 각 지역의 데이터를 표현하는 모델
class Region(BaseModel):
    name: str  # 구역 이름
    area: float = Field(
        gt=0, description="면적은 0보다 커야 합니다."
    )
    altitude: float = Field(
        gt=0, lt=9000, description="고도는 0~9000m 사이여야 합니다."
    )

# 🌿 여러 지역 데이터를 묶은 전체 입력 구조
class ForestData(BaseModel):
    regions: List[Region]
