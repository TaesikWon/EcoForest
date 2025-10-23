# app/service.py

"""
ForestEcoAI - 산림 데이터 간단 분석 모듈
(지금은 기본 구조용, 나중에 GeoPandas 분석으로 확장 가능)
"""

def analyze_forest_data(data: list[dict]) -> dict:
    """
    입력 데이터 예시:
    [
        {"area": 120, "altitude": 300},
        {"area": 90, "altitude": 280},
        {"area": 150, "altitude": 350}
    ]

    출력 예시:
    {
        "total_area": 360,
        "average_altitude": 310.0,
        "message": "산림 데이터 분석 완료 ✅"
    }
    """

    # 예외 처리
    if not data:
        return {"error": "입력된 데이터가 없습니다."}

    # 총 면적과 평균 고도 계산
    total_area = sum(item.get("area", 0) for item in data)
    avg_altitude = sum(item.get("altitude", 0) for item in data) / len(data)

    # 결과 리턴
    return {
        "total_area": round(total_area, 2),
        "average_altitude": round(avg_altitude, 2),
        "message": "산림 데이터 분석 완료 ✅"
    }
