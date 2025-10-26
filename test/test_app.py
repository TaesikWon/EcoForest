import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# ✅ 정상 입력 테스트
def test_eco_analyze_success():
    """
    정상적인 생태 데이터 입력 시 eco_result.html이 잘 표시되는지 확인
    """
    data = {
        "name": "백두산 남사면",
        "area": "1200",
        "altitude": "350"
    }
    response = client.post("/eco/analyze", data=data)

    # 요청이 성공적으로 처리되어야 함
    assert response.status_code == 200
    # 결과 페이지 주요 문구 확인
    assert "면적" in response.text
    assert "고도" in response.text


# ✅ 잘못된 입력 테스트 (유효성 검사 실패 시 ValidationError 발생)
def test_eco_analyze_invalid_input():
    """
    음수 면적 등 잘못된 입력 시, Pydantic ValidationError가 발생하는지 확인
    """
    data = {
        "name": "오류지대",
        "area": "-100",        # ❌ 음수값 — 검증 실패 예상
        "altitude": "99999"    # ❌ 비정상 고도
    }

    # ✅ ValidationError 발생이 "정상 동작"임
    with pytest.raises(Exception) as e:
        client.post("/eco/analyze", data=data)

    # ✅ 예외 메시지 내용 확인 (면적 조건 실패 메시지 포함)
    assert "greater than" in str(e.value) or "ValidationError" in str(e.value)
