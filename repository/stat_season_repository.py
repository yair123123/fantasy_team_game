

from models.stat_season import StatSeason
from repository.database import get_db_connection


def getAll():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM stat_season
            """      )
        rows = cursor.fetchall()
        stat_seasons = [StatSeason(**f) for f in rows]
        return stat_seasons


def getById(stat_season_id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM stat_season WHERE id = %s", (stat_season_id,))
        stat_season = cursor.fetchone()
        if stat_season is None:
            return None
        stat_season = StatSeason(**stat_season)
        return stat_season
def getBy_player_Id(player_id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM stat_season WHERE player_id = %s", (player_id,))
        stat_season = cursor.fetchall()
        if stat_season is None:
            return None
        stat_seasons = [StatSeason(**f) for f in stat_season]
        return stat_seasons


def create(state:StatSeason) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO stat_season (season,player_id,position,team,points,games,twoPercent,threePercent,atr,ppgRatio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id
            """,
            (state.season,state.player_id,state.position,state.team,state.points,state.games,state.twopercent,state.threepercent,state.atr,state.ppgratio)
        )
        connection.commit()
        state_id = cursor.fetchone()["id"]
        return state_id
def update(state:StatSeason,user_id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE stat_season SET season = %s,player_id = %s,position = %s,team = %s,points = %s,games = %s,twoPercent = %s,threePercent = %s,atr = %s,ppgRatio = %s WHERE id = %s
            """,
            (state.season,state.player_id,state.position,state.team,state.points,state.games,state.twopercent,state.threepercent,state.atr,state.ppgratio,user_id)
        )
        connection.commit()
        return getById(user_id)

def delete(id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            DELETE FROM stat_season WHERE id = %s
            """,
            (id,)
        )
        connection.commit()