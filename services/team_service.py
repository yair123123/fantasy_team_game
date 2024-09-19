from typing import List

from toolz import unique

from models.player import Player
from models.team import Team
from repository import player_repository, team_repository


def validation(team: List[Player]) -> bool:
    valid_players = [player for player in team if player is not None]
    a = len(valid_players)
    if len(valid_players) < 5:
        return False
    unique_positions = list(unique(player.position for player in valid_players))
    a = len(unique_positions)
    breakpoint()
    return len(unique_positions) == 5
def create_team(team:Team):
    players = list(map( lambda x:player_repository.getById(x),team.players_ids))
    if validation(players):
        return team_repository.create(team)
    else:
        return None
def update_team(team:Team,id:int):
    players = list(map( lambda x:player_repository.getById(x),team.players_ids))
    if validation(players):
        return team_repository.update(team,id)
    else:
        return None