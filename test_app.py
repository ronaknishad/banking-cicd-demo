import pytest
from app import app, calculate_emi


@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Banking App API is running"


def test_health(client):
    res = client.get("/health")
    assert res.get_json() == {"status": "ok"}


def test_emi_value():
    assert calculate_emi(100000, 10.0, 12) == 8791.60


def test_emi_zero_interest():
    assert calculate_emi(12000, 0, 12) == 1000.0


def test_emi_invalid_input():
    with pytest.raises(ValueError):
        calculate_emi(0, 10.0, 12)


def test_emi_endpoint(client):
    res = client.get("/emi/100000/10.0/12")
    assert res.get_json()["emi"] == 8791.59
