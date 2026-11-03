
from fastapi import FastAPI

from .schemas import DraftScenario

app = FastAPI(
    title="LeagueShift API",
    description="NBA Expansion Strategy & Optimization",
    version="0.1.0",
)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "project": "LeagueShift",
    }


@app.get(
    "/api/scenarios/default",
    response_model=DraftScenario,
)
def default_scenario() -> DraftScenario:
    return DraftScenario(
        name=(
            "2004-inspired hypothetical baseline "
            "(not official 2028 rules)"
        ),
        draft_year=2028,
        expansion_teams=["Seattle", "Las Vegas"],
        protected_players_per_team=8,
        max_losses_per_existing_team=1,
        two_way_players_eligible=False,
    )
