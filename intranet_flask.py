"""
Intranet Flask Routes
Michael Piscione
CS 2660/Fall 2023

TODO: Write this
"""

# Dependencies
from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__, static_folder='static')


@app.route("/", methods=['GET', 'POST'])
def login():
    """Intranet Login Page """
    return render_template("index.html")


@app.route("/intranet_menu")
def intranet_menu():
    """ Intranet Menu Page """
    return render_template("intranet_menu.html")
