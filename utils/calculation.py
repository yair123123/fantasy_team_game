from typing import List, Dict

from toolz import pipe


def calculation_atr(assists, turnovers):
    if assists == 0 or turnovers == 0:
        return 0
    return assists / turnovers
def calculation_ppg_ratio(players,player):
    players_on_position = filter(lambda x:x['position'] == player['position'],players)
    points_per_game = lambda x:x['points'] / x['games']
    avg = average(list(map(points_per_game,players_on_position)))
    return points_per_game(player) / avg 
def average(x):
    return sum(x) / len(x)


def team_ppg_calculation(teams: List[Dict]) -> List[Dict]:
    team_ppg = pipe(
        teams,
        lambda y: [
            {
                'team_id': team['team'][0]['id'],
                'team_name': team['team'][0]['name_team'],
                'ppg_sum': sum(player['ppgratio'] for player in team['players'])
            }
            for team in y
        ]
    )

    sorted_team_ppg = sorted(team_ppg, key=lambda x: x['ppg_sum'], reverse=True)

    return sorted_team_ppg

    return team_ppg