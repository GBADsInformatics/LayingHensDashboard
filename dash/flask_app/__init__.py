"""Initialize Flask app."""
from flask import Flask
SECRET_KEY = 'ThisIsTheSecretKey'

def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.secret_key = SECRET_KEY
    app.debug = True
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        # Import Dash application
        from .plotlydash.dashboard import init_dashboard
        app = init_dashboard(app)

        return app