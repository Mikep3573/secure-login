"""
Intranet Flask Routes
Michael Piscione
CS 2660/Fall 2023

TODO: Write this
"""

# Dependencies
from flask import Flask, render_template, request, redirect
from database_funcs import *
from gen_functions import *

# Create a Flask app
app = Flask(__name__, static_folder='static')


@app.route("/", methods=["GET", "POST"])
def login():
    """ TODO: Write this """
    # Get the request method
    request_method = request.method
    if request_method == "POST":  # Check if it's a POST method
        # Get the username/password submitted
        username = request.form.get("username")
        password = request.form.get("password")
        create_pass = request.form.get("create_pass")
        print(create_pass)

        # Check if that combination does not exist in the database, redirect to /intranet_menu if it does
        if check_user_info(username, password) == AccessType.NULL:
            return render_template("index.html", incorrect=True)
        else:
            return redirect("/intranet_menu")

    # Check if the user wanted to generate a strong password
    create_pass = request.args.get("create_pass")
    if create_pass:
        return render_template("index.html",
                               create_pass=True, password=create_password(), incorrect=False)

    return render_template("index.html")  # Render index.html if GET method and create_pass != True


@app.route("/intranet_menu")
def intranet_menu():
    """ Intranet Menu Page """
    return render_template("intranet_menu.html")


@app.route("/accepted_choice")
def accepted_choice():
    """ Displays when user is allowed to visit menu choice """
    return render_template("accepted_choice.html")
