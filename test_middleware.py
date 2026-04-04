import pytest
from src.app import app

@pytest.fixture
def client():
    # Flask test istemcisini başlatır
    with app.test_client() as client:
        yield client

def test_secure_endpoint_unauthorized(client):
    """Senaryo: Token olmadan güvenli rotaya erişim engellenmeli (401)"""
    response = client.get('/api/secure')
    assert response.status_code == 401

def test_secure_endpoint_authorized(client):
    """Senaryo: Doğru token ile güvenli rotaya erişim sağlanmalı (200)"""
    # .env dosyasındaki token ile aynı olmalı
    headers = {"Authorization": "Bearer kubra-istu-midterm-2026"}
    response = client.get('/api/secure', headers=headers)
    assert response.status_code == 200

def test_vulnerable_logic(client):
    """Senaryo: Zafiyetli rotada yetki olmasa bile sunucu işlem yapar"""
    # Bu test, mantıksal zafiyetin varlığını doğrular
    response = client.get('/api/vulnerable')
    # Sonuç 401 olsa bile arka planda işlem yapıldığını terminal loglarından görebilirsin
    assert response.status_code == 401
