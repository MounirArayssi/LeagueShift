
from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_default_scenario() -> None:
    response = client.get("/api/scenarios/default")

    assert response.status_code == 200

    scenario = response.json()

    assert scenario["draft_year"] == 2028
    assert scenario["protected_players_per_team"] == 8
    assert scenario["expansion_teams"] == [
        "Seattle",
        "Las Vegas",
    ]
