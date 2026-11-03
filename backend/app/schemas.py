
from datetime import date
from typing import Literal

from pydantic import BaseModel, Field, HttpUrl


class DraftScenario(BaseModel):
    name: str
    draft_year: int = Field(ge=2026)
    expansion_teams: list[str] = Field(min_length=1)
    protected_players_per_team: int = Field(ge=1, le=20)
    max_losses_per_existing_team: int = Field(ge=1, le=2)
    two_way_players_eligible: bool


class ContractRecord(BaseModel):
    player_id: str
    team_id: str
    season: str

    salary_usd: int | None = Field(default=None, ge=0)
    guaranteed_salary_usd: int | None = Field(
        default=None, ge=0
    )

    option_type: Literal[
        "none", "team", "player", "mutual", "unknown"
    ] = "unknown"

    status: Literal[
        "signed", "conditional", "expired", "unknown"
    ] = "unknown"

    as_of: date
    source_url: HttpUrl | None = None
