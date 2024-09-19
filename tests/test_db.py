import pytest
from models.player import Player
from repository.database import get_db_connection, create_tables, drop_all_tables
from repository.player_repository import getAll, getById, create, update, delete, get_by_position
@pytest.fixture(scope='module')
def setup_database():
    create_tables()
    yield
    drop_all_tables()

def test_create_player(setup_database):
    new_player = Player(id=1, player_name="John Doe", position="C", points=20, games=5)
    player_id = create(new_player)
    assert player_id == "1"

def test_get_all_players(setup_database):
    new_player = Player(id=1, player_name="John Doe", position="C", points=20, games=5)
    create(new_player)
    players = getAll()
    assert isinstance(players, list)
    assert len(players) > 0

def test_get_player_by_id(setup_database):
    new_player = Player(id=1, player_name="John Doe", position="C", points=20, games=5)
    create(new_player)
    player = getById("1")
    assert player is not None
    assert player.player_name == "John Doe"

def test_update_player(setup_database):
    new_player = Player(id=1, player_name="John Doe", position="C", points=20, games=5)
    create(new_player)
    player = Player(id=1, player_name="John Doe", position="C", points=20, games=5)
    player.ppgratio = 15.0
    updated_player = update(player, "1")
    assert updated_player.ppgratio == 15.0

def test_delete_player(setup_database):
    delete("1")
    player = getById("1")
    assert player is None

def test_get_by_position(setup_database):
    players = get_by_position("Forward")
    assert isinstance(players, list)
    assert all(player.position == "Forward" for player in players)
