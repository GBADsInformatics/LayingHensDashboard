from flask_app import init_app
from os import environ as env

app = init_app()

def returnApp():
    return app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=env.get('PORT', 8050) , debug=env.get('DEBUG', 'false').lower() in ('true', '1', 't'))