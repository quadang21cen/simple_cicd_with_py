# test_app.py
from app import app

def test_hello_world():
    """Kiểm tra xem trang chủ có trả về đúng nội dung và status code không."""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, CI/CD with GitHub Actions!' in response.data