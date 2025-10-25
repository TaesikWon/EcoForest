# test_app.py
from fastapi.testclient import TestClient
from main import app

# FastAPI 앱을 테스트할 클라이언트 생성
client = TestClient(app)

# ✅ 정상 입력 테스트
def test_analyze_success():
    """
    올바른 데이터 입력 시, 결과 페이지(result.html)가 잘 표시되는지 확인
    """
    data = {
        "area1": "100", "altitude1": "300",
        "area2": "200", "altitude2": "400",
        "area3": "150", "altitude3": "250"
    }
    response = client.post("/analyze", data=data)

    # 요청이 성공적으로 처리되어야 함
    assert response.status_code == 200
    # 결과 페이지에 포함될 내용 일부 확인
    assert "분석 결과" in response.text
    assert "총 면적" in response.text
    assert "평균 고도" in response.text


# ❌ 오류 입력 테스트 (음수나 과도한 값)
def test_analyze_invalid_input():
    """
    잘못된 입력(음수나 9000m 초과 고도) 시 error.html이 잘 표시되는지 확인
    """
    data = {
        "area1": "-50", "altitude1": "300",
        "area2": "200", "altitude2": "9500",  # 고도 초과
        "area3": "150", "altitude3": "250"
    }
    response = client.post("/analyze", data=data)

    # 요청 자체는 200이어야 하지만, 결과는 error.html이어야 함
    assert response.status_code == 200
    # 오류 페이지에 들어갈 문구 일부 확인
    assert "오류" in response.text or "입력값" in response.text or "error" in response.text
