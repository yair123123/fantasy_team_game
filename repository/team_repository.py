from flask import jsonify

from models.team import Team
from repository.database import get_db_connection
from repository.player_repository import getById


def findAll():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM questions
            """      )
        rows = cursor.fetchall()
        questions = [Team(**f) for f in rows]
        return questions


def findById(id:int):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT *
                FROM team
                WHERE id = %s;
            """, (id,))

            team = cur.fetchall()
            if not team:
                return None
            cur.execute("""
                SELECT p.*
                FROM players p
                JOIN team_players tp ON p.id = tp.player_id
                WHERE tp.team_id = %s;
            """, (id,))
            players = cur.fetchall()
            return {
                'team': team,
                'players': players
            }

def create(team:Team) -> int:
    with get_db_connection() as connection, connection.cursor() as cur:
        cur.execute("INSERT INTO team (name_team) VALUES (%s) RETURNING id;", (team.name_team,))
        team_id = cur.fetchone()['id']
        for player in team.players_ids:
            cur.execute("""
                INSERT INTO team_players (team_id, player_id)
                VALUES (%s, %s);
        """, (team_id, player))
        connection.commit()
        return team_id
def update(team:Team,id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("""
            UPDATE team 
            SET name_team = %s 
            WHERE id = %s;
        """,
        (team.name_team, id)
                    )

        cursor.execute("""
            DELETE FROM team_players 
            WHERE team_id = %s;
        """, (id,))

        # 2. הוסף את השחקנים החדשים
        for player_id in team.players_ids:
            cursor.execute("""
                INSERT INTO team_players (team_id, player_id)
                VALUES (%s, %s);
            """, (id, player_id))
        connection.commit()
        return findById(id)

def delete(id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT 1 FROM team_players WHERE id = %s", (id,))
        if cursor.fetchone():
            cursor.execute("DELETE FROM team_players WHERE id = %s", (id,))
            return True
        else:
            return False