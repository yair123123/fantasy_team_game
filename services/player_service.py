from typing import List
from toolz import pipe
from toolz.curried import unique
from models.player import Player
from utils.player import get_position, get_games, get_points, get_twoPercent, get_threePercent, get_atr, get_ppg_ratio
from repository.player_repository import update, getAll


def p(a):
    print(len(a))
    return a

def get_only_players(players: List[dict[str, str]]):
    list_instance = pipe(
        players,
        unique(key=lambda x: x['playerId']),
    )
    obj = []
    for y in list_instance:
        new =Player(player_name=y['playerName'],
        id=y['playerId'],
        position=get_position(y, players),
        games=get_games(y, players),
        points=get_points(y, players))
        obj.append(new)
    return obj

def update_all_players():
    players = getAll()
    list(map(update_calculation,players))
def update_calculation(player:Player):
    new_player = Player(player_name=player.player_name, id=player.id, position=player.position,games=player.games,points=player.points,twopercent=get_twoPercent(player),threepercent=get_threePercent(player),atr=get_atr(player),ppgratio=get_ppg_ratio(player))

    update(new_player,player.id)