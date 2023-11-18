"""
Intranet Flask Routes
Michael Piscione
CS 2660/Fall 2023

TODO: Write this
"""

# Dependencies
from flask import Flask, render_template, request
from database_funcs import *

# Create a Flask app
app = Flask(__name__, static_folder='static')


@app.route("/", methods=["GET", "POST"])
def login():
    """Intranet Login Page """
    user_bool = True
    pass_bool = True
    request_method = request.method
    if request_method == "POST":
        print('---------')
        print(request.form)
        print('---------')
    return render_template("index.html", user_bool=user_bool, pass_bool=pass_bool)


@app.route("/intranet_menu")
def intranet_menu():
    """ Intranet Menu Page """
    return render_template("intranet_menu.html")


@app.route("/accepted_choice")
def accepted_choice():
    """ Displays when user is allowed to visit menu choice """
    return render_template("accepted_choice.html")
