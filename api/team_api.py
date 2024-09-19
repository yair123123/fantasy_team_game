
from typing import List, Dict
import requests



def get_from_api(url):
    response = requests.get(url)
    return response.json()

def get_players_by_year(year:int) -> List[Dict[str, str]]:
    players = get_from_api(f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={year}&&pageSize=100")
    # if questions_and_answers['response_code'] == 5:
    #     return get_questions_and_answers()
    return players
def get_all_players() -> List[Dict[str, str]]:
    players = get_from_api("http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2022&&pageSize=100")
    # if questions_and_answers['response_code'] == 5:
    #     return get_questions_and_answers()
    return players

