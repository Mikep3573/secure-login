"""
Intranet Flask Routes
Michael Piscione
CS 2660/Fall 2023

Holds all the necessary functionality that occurs when a user moves to a certain route. Includes login functionality,
registering functionality, and the menu functionality.
"""

# Dependencies
from flask import Flask, render_template, request, redirect
from database_funcs import *
from gen_functions import *

# Create a global Flask app
app = Flask(__name__, static_folder='static')

# Create a global login counter
# NOTE: must restart app in order to reset attempts after 3 failed logins
attempts = 0


@app.route("/", methods=["GET", "POST"])
def login():
    """ login gets the username and password in a POST request, checks the information, and returns either
     the menu (with their access type as a parameter) or the login menu again with failed attempts incremented.
     If it is a GET request with the create_pass boolean flag set, it returns a randomly generated strong password.
     If it is just a GET request with nothing else, it loads the login menu at its default state. """
    # Make sure we're looking at the correct attempts
    global attempts

    # Get the request method
    request_method = request.method

    # Check if it's a POST method
    if request_method == "POST":
        # Get the username/password submitted
        username = request.form.get("username")
        password = request.form.get("password")

        # Check access type of user (null if no account)
        access_type = check_user_info(username, password)

        # Check if that combination does not exist in the database, redirect to /intranet_menu if it does
        if access_type == AccessType.NULL:
            attempts += 1  # Increment attempts for every successive failed login
            return render_template("index.html", incorrect=True, attempts=attempts)
        else:
            attempts = 0  # Reset attempts on successful login
            return redirect(f"/intranet_menu?access_type={access_type}")

    # Check if the user wanted to generate a strong password and render accordingly
    create_pass = request.args.get("create_pass")
    if create_pass:
        return render_template("index.html", attempts=attempts,
                               create_pass=True, password=create_password())

    # Render index.html if GET method and create_pass != True
    return render_template("index.html", attempts=attempts)


@app.route("/register", methods=["GET", "POST"])
def register():
    """ register gets the username and password in a POST request. It checks that that username is available,
     and that the password entered is acceptable. If both are true it inserts the new user into the 'users' table
     with the NONE access type by default. If it is a GET request with the create_pass boolean flag set, it returns
     a randomly generated strong password. If it is just a GET request with nothing else, it loads the register menu at
     its default state."""
    # Make sure we're looking at the correct attempts
    global attempts

    # Get the request method
    request_method = request.method

    # Check if it's a POST method
    if request_method == "POST":
        # Get the username/password submitted
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if that combination does not exist in the database, register new account if it doesn't
        if check_user_info(username, password) == AccessType.NULL:
            # Check if valid password
            if not check_password(password):
                # Render register.html with invalid password dialogue
                return render_template("register.html", attempts=attempts, invalid_pass=True)
            else:
                # Attempt to insert new user info with 'none' access type
                if not insert_user_info(username, password, AccessType.NONE):
                    # If username already taken, give failure message
                    return render_template("register.html", attempts=attempts, invalid_user=True)
                else:
                    # Reset attempts so user can log in with new account
                    attempts = 0
                    # If username not already taken, give success message
                    return render_template("register.html", attempts=attempts, invalid_user=False)

    # Check if the user wanted to generate a strong password and render accordingly
    create_pass = request.args.get("create_pass")
    if create_pass:
        return render_template("register.html", attempts=attempts,
                               create_pass=True, password=create_password())

    # Render register.html normally
    return render_template("register.html", attempts=attempts)


@app.route("/intranet_menu")
def intranet_menu():
    """ intranet_menu simply displays only the menu options available given a certain access_type. """
    # Get the user's access type
    access_type = request.args.get("access_type")

    # Render intranet menu with appropriate options
    return render_template("intranet_menu.html", access_type=access_type)


@app.route("/accepted_choice")
def accepted_choice():
    """ accepted_choice simply displays a message once the user selects a menu option. """
    return render_template("accepted_choice.html")
