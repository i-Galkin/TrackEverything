"""
This script runs the TrackEverything application using a development server.
"""

import os
from TrackEverything import create_app
from os import environ

# Should exec: export FLASK_CONFIG=development && export FLASK_APP=run.py
# config_name = os.getenv('FLASK_CONFIG')
app = create_app('development')

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
