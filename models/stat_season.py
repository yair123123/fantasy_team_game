from dataclasses import dataclass


@dataclass
class StatSeason:
    season : str
    player_id : int
    position: str
    team : str
    points : int
    games : int
    twopercent : float
    threepercent : float
    atr : float
    ppgratio: float
    id: int = None
