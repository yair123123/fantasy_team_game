from dataclasses import dataclass
from typing import List


@dataclass
class Team:
    name_team : str
    players_ids : List[str]
    id:int = None
