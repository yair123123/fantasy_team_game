from api.team_api import get_players_by_year
from repository import player_repository, stat_season_repository
from repository.database import create_tables, tables_exist
from services.player_service import get_only_players, update_all_players
from services.stat_season_service import get_only_stat_season

def start():
    if not tables_exist():
        create_tables()
        get_all_and_save()
        update_all_players()



def get_all_players_and_state():
    years = [2022,2023,2024]
    players =  list(map(lambda x: get_players_by_year(x),years))
    combined_list = sum(players, [])
    only_players = get_only_players(combined_list)
    only_stat = get_only_stat_season(combined_list)
    return only_players,only_stat

def save_players_db(only_players):
    list(map(player_repository.create, only_players))
def save_state_to_db(only_stat):
    list(map(stat_season_repository.create, only_stat))
def get_all_and_save():
    a = get_all_players_and_state()
    save_players_db(a[0])
    save_state_to_db(a[1])