from flask import Blueprint, jsonify, request
from repository import team_repository as re
from utils.calculation import team_ppg_calculation

stats_blueprint = Blueprint('stats', __name__)

@stats_blueprint.route('/', methods=['GET'])
def compare():
    breakpoint()
    teams = request.args.getlist('team_id')
    if not teams or len(teams) < 2:
        return jsonify({'error': "dont have enough teams"}), 400

    teams_data = []
    for team_id in teams:
        team = re.findById(int(team_id))
        if team:
            teams_data.append(team)
        else:
            return jsonify({'error': f'team {team_id} not found'}), 404

    team_sorted = team_ppg_calculation(teams_data)
    return jsonify(team_sorted)
