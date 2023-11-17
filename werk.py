"""
Werkzeug Launcher
Michael Piscione
CS 2660/Fall 2023

Werkzeug launcher for application. Simply launches the flask app.

NOTE: Same werkzeug launcher as used in bank labs with minor changes.
"""

# Dependencies
import traceback
from intranet_flask import app


def main():
    """ Creating a main for aesthetic purposes. """
    try:  # Attempt to run the Flask app using localhost port 8097 (temporary port)
        app.run(debug=app.debug, host='localhost', port=8097)
    except Exception:  # Print any errors that occur on launch
        traceback.print_exc()


if __name__ == '__main__':
    main()
