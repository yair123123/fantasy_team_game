from flask import blueprints, jsonify, request
from models.team import Team
from repository import team_repository as re
from repository.team_repository import delete
from services.team_service import create_team, update_team

team_blueprint = blueprints.Blueprint('teams', __name__)

@team_blueprint.route('/<int:id>', methods=['GET'])
def findById(id:int):
    team = re.findById(id)
    return jsonify(team),200
@team_blueprint.route('/', methods=['POST'])
def create():
    a = request.json
    team = Team(**a)
    id = create_team(team)
    if id is None:
        return jsonify({"error": "Invalid players."}), 400
    return jsonify(id),201

@team_blueprint.route('/<int:id>', methods=['PUT'])
def update(id:int):
    a = request.json()
    new_team = Team(**a)
    new_team = update_team(new_team,id)
    return jsonify(new_team),200

@team_blueprint.route('/{id}', methods=['DELETE'])
def delete_team(id:int):
    done = delete(id)
    if not done:
        return jsonify({"error": "No team found."}), 404
    return jsonify({}),200