from fastapi.testclient import TestClient

from api.main import app
from api.routes import laptops

client = TestClient(app)


def test_get_laptops_ok(monkeypatch):
    async def fake_get_portatilesModelo(skip: int, total: int, filtronombre=None):
        return {
            "portatiles": [
                {"id": 1, "modelo": "MacBook Air", "precio": 1200, "OS": "mac"},
                {"id": 2, "modelo": "ThinkPad", "precio": 900, "OS": "windows"},
            ]
        }

    monkeypatch.setattr(laptops.portatil_data, "get_portatilesModelo", fake_get_portatilesModelo)

    response = client.get("/laptops/?skip=0&total=2&filtroNombre=Book")

    assert response.status_code == 200
    data = response.json()
    assert "portatiles" in data
    assert len(data["portatiles"]) == 2


def test_get_laptop_by_id_ok(monkeypatch):
    async def fake_get_portatil(portatil_id: int):
        return {"id": portatil_id, "modelo": "XPS 13", "precio": 1500, "OS": "windows"}

    monkeypatch.setattr(laptops.portatil_data, "get_portatil", fake_get_portatil)

    response = client.get("/laptops/10")

    assert response.status_code == 200
    assert response.json()["id"] == 10


def test_create_laptop_post_ok(monkeypatch):
    async def fake_write_portatil(portatil):
        payload = portatil.model_dump()
        payload["id"] = 999
        return payload

    monkeypatch.setattr(laptops.portatil_data, "write_portatil", fake_write_portatil)

    response = client.post(
        "/laptops/",
        json={
            "modelo": "Legion 5",
            "precio": 1300,
            "OS": "windows",
            "marcagpu": "nvidia",
            "memoriaram": 16,
        },
    )

    assert response.status_code == 201
    assert response.json()["id"] == 999


def test_delete_laptop_ok(monkeypatch):
    async def fake_delete_portatil(portatil_id: int):
        return {"info": f"borrado portatil {portatil_id}"}

    monkeypatch.setattr(laptops.portatil_data, "delete_portatil", fake_delete_portatil)

    response = client.delete("/laptops/3")

    assert response.status_code == 200
    assert response.json()["info"] == "borrado portatil 3"
