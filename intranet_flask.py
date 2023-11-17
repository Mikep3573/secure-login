"""
Intranet Flask Routes
Michael Piscione
CS 2660/Fall 2023

TODO: Write this
"""

# Dependencies
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__, static_folder='instance/static')

# Configure Flask app
app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def login():
    """Intranet Login Page """
    return render_template('login.html',
                           title="Company Intranet Login",
                           heading="Company Intranet Login")
