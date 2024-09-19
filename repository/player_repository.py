from bdb import Breakpoint

from models.player import Player
from repository.database import get_db_connection


def getAll():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM players
            """      )
        rows = cursor.fetchall()
        users = [Player(**f) for f in rows]
        return users


def getById(player_id:str):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM players WHERE id = %s", (player_id,))
        player = cursor.fetchone()
        if player is None:
            return None
        player = Player(**player)
        return player


def create(player:Player) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO players (id,player_name,position,points,games) VALUES (%s,%s,%s,%s,%s) returning id
            """,
            (player.id,player.player_name,player.position,player.points,player.games)
        )
        connection.commit()
        player_id = cursor.fetchone()["id"]
        return player_id
def update(player:Player,player_id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE players SET ppgratio = %s,atr = %s,twopercent = %s,threepercent = %s WHERE id = %s
            """,
            (player.ppgratio,player.atr,player.twopercent,player.threepercent,player_id)
        )
        connection.commit()
        return getById(player_id)

def delete(id:str):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            DELETE FROM players WHERE id = %s
            """,
            (id,)
        )
        connection.commit()

def get_by_position(position:str):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM players WHERE position = %s
            """,
            (position,)
        )
        rows = cursor.fetchall()
        users = [Player(**f) for f in rows]
        return users