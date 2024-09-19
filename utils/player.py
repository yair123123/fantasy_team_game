from functools import partial
from operator import itemgetter
from toolz import pipe
from repository import player_repository, stat_season_repository
from utils.calculation import average

def get_position(player, players):
    try:
        return pipe(
            players,
            partial(filter,lambda x: x['playerId'] == player['playerId']),
            partial(filter,lambda x: x['season'] == 2024),
            partial(map,itemgetter('position')),
            next,
        )
    except StopIteration:
        return player['position']

def get_points(player, players):
    return pipe(
        players,
        partial(filter,lambda x: x['playerId'] == player['playerId']),
        partial(map,itemgetter('points')),
        sum,
    )

def get_games(player, players):
    return pipe(
        players,
        partial(filter,lambda x: x['playerId'] == player['playerId']),
        partial(map,itemgetter('games')),
        sum,
    )


def get_average_stat(player, stat_key):
    players = stat_season_repository.getBy_player_Id(player.id)

    if players:
        total = sum(getattr(x, stat_key) if getattr(x, stat_key) is not None else 0 for x in players)
        count = len(players)
        return total / count

    return 0


def get_atr(player):
    return get_average_stat(player, 'atr')

def get_twoPercent(player):
    return get_average_stat(player, 'twopercent')

def get_threePercent(player):
    return get_average_stat(player, 'threepercent')

def get_ppg_ratio(player):
    return get_average_stat(player, 'ppgratio')
