from typing import List
from toolz import pipe

from models.player import Player
from models.stat_season import StatSeason
from utils.calculation import calculation_atr, calculation_ppg_ratio


def get_only_stat_season(players:List[dict]):
    return pipe(
        players,
        lambda x: map(lambda y: StatSeason(
            season=y['season'],
            player_id=y['playerId'],
            position=y['position'],
            team=y['team'],
            points=y['points'],
            games=y['games'],
            twopercent=y['twoPercent'],
            threepercent=y['threePercent'],
            atr = calculation_atr(y['assists'],y['turnovers']),
            ppgratio=calculation_ppg_ratio(players,y),
                                           ),x)
        ,list
    )