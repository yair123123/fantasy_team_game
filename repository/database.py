import psycopg2
from psycopg2.extras import RealDictCursor
from Config.sql_config import SQLALCHEMY_DATABASE_URI


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI,cursor_factory=RealDictCursor)
def tables_exist():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
            """)
            tables = {row['table_name'] for row in cur.fetchall()}
            return len(tables) == 4

def create_tables():
    with get_db_connection() as conn, conn.cursor() as cur:
        cur.execute(""" 
        CREATE TABLE IF NOT EXISTS players (
            id varchar(100) PRIMARY KEY,
            player_name varchar(100) NOT NULL,
            position varchar(100) NOT NULL,
            points int,
            games int,
            twoPercent float,
            threePercent float,
            atr float,
            ppgRatio float

        );
        """)

        cur.execute(""" 
        CREATE TABLE IF NOT EXISTS stat_season (
            id SERIAL PRIMARY KEY,
            season int NOT NULL,
            position varchar(100) NOT NULL,
            team varchar(100) NOT NULL,           
            points int NOT NULL,
            games int NOT NULL,
            twoPercent float,
            threePercent float,
            atr float NOT NULL,
            ppgRatio float NOT NULL,
            player_id varchar(100) NOT NULL,
            FOREIGN KEY(player_id) REFERENCES players(id) ON DELETE CASCADE
        );
        """)

        cur.execute(""" 
        CREATE TABLE IF NOT EXISTS team (
            id SERIAL PRIMARY KEY,
            name_team varchar(100) NOT NULL
        );
        """)

        cur.execute(""" 
        CREATE TABLE IF NOT EXISTS team_players (
            team_id int NOT NULL,
            player_id varchar(100) NOT NULL,
            FOREIGN KEY (team_id) REFERENCES team(id) ON DELETE CASCADE,
            FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
        );
        """)

        conn.commit()


def drop_all_tables():
    with get_db_connection() as conn, conn.cursor() as cur:
        try:
            cur.execute("DROP TABLE IF EXISTS players,stat_season,team,team_players CASCADE;")
        except :
            drop_all_tables()
        conn.commit()