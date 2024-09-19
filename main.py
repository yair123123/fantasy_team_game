from flask import Flask
from controllers.compare import stats_blueprint
from controllers.fantasi_cntroller import team_blueprint
from controllers.players_controller import players_blueprint
from repository.player_repository import getAll
from services.main_service import start

app =Flask(__name__)
app.register_blueprint(team_blueprint, url_prefix='/api/teams')
app.register_blueprint(players_blueprint, url_prefix='/api/players')
app.register_blueprint(stats_blueprint, url_prefix='/api/stats')


if __name__ == "__main__":
    start()
    app.run(debug=True)