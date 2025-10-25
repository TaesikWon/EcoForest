from pydantic import BaseModel, Field
from typing import Optional, Dict

class GeoRegion(BaseModel):
    name: str
    latitude: float = Field(..., description="위도")
    longitude: float = Field(..., description="경도")
    population: int = Field(gt=0, description="인구수 (명)")
    population_density: float = Field(gt=0, description="인구밀도 (명/km²)")
    category: str = "urban"
    metadata: Optional[Dict] = Field(default_factory=dict, description="추가 메타데이터")