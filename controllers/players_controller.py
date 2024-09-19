from dataclasses import asdict
from flask import blueprints, jsonify, request

from models.player import Player
from repository import player_repository as re
from repository import stat_season_repository as an

players_blueprint = blueprints.Blueprint('players', __name__)

@players_blueprint.route('/<int:id>', methods=['GET'])
def findById(id:str):
    player = asdict(re.getById(id))
    return jsonify(player),200

@players_blueprint.route('/', methods=['GET'])
def find_by_position():
    players = (re.get_by_position(request.args.get('position')))
    players = list(map(asdict,players))
    return jsonify(players),200

