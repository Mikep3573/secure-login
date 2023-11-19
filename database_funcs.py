"""
Database Functions
Michael Piscione
CS 2660/Fall 2023

Database Functions consists of mainly general purpose functions meant to interact with a database called
'intranet_users', specifically the table labeled 'users'. It creates and queries the database via the Python SQLite API.

NOTE: Some of this code comes from Prof. Eddy's SQLite example.
"""

# Dependencies
import sqlite3
from classes.access_types import *
from gen_functions import *

# Database Made constant -> used to determine whether to create database
DB_MADE = False


def create_db() -> bool:
    """ Creates the 'intranet_users' database (for usernames and passwords) with a table 'users'. Returns True if
    created successfully (or already exists), False otherwise. Takes nothing as input. """
    # Check if table exists before creating the table
    if not check_table("users"):
        # Attempt to create Database
        try:
            conn = sqlite3.connect('db/intranet_users.db')  # Connect to intranet_users.db
            cur = conn.cursor()  # Create a cursor for the database

            # Initialize the database to have a table of users with columns representing username, password, access_type
            # Ensure no two users can have the same username
            cur.execute("CREATE TABLE users(username text UNIQUE, password text, access_type text)")

            # Commit the table
            conn.commit()

            # Successfully completed
            return True

        # Do exception handling
        except BaseException:  # Return False upon unsuccessful completion (or database has been created already)
            return False
        finally:  # Close the objects
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
    else:  # Return True, table already exists
        return True


def check_user_info(username: str, password: str) -> AccessType:
    """ Queries database using input username for WHERE clause. Returns entry containing that username.
     If an entry contains BOTH the provided username and password, return their access type. Returns
     a NULL access type if none found or on error exception. NOTE: username is a UNIQUE field. Still
     included for-loop in case, at some point, we allow usernames to not be UNIQUE. """

    # Attempt to query database
    try:
        # Connect to database and establish a cursor
        conn = sqlite3.connect('db/intranet_users.db')
        cur = conn.cursor()

        # Query for entries containing that username
        for row in cur.execute("SELECT * FROM users WHERE username = ?", [username]):
            if row[0] == username and row[1] == password:
                return convert_access_type(row[2])  # If entry found, return it's AccessType

        # If no entry found matching description
        return AccessType.NULL  # Signifies no access type

    # Print helpful error message upon unsuccessful completion
    except BaseException:
        print("ERROR: Could not connect to database")
        return AccessType.NULL  # Signifies no access type
    finally:  # Close the objects
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def insert_user_info(username: str, password: str, access_type: AccessType) -> bool:
    """ Creates a new row in users table using the username, password, and access_level of a new user.
    Each row is of the form username, password, access_level. Returns True or False upon successful or failed
    insertion. """

    # Attempt to insert validated user input
    try:
        conn = sqlite3.connect('db/intranet_users.db')  # Connect to intranet_users.db
        cur = conn.cursor()  # Create a cursor for the database

        # Store data to insert into table
        user_data = [
            (username, password, access_type)
        ]

        # Attempt to insert user data
        cur.executemany("INSERT INTO users VALUES(?, ?, ?)", user_data)

        # Commit the changes
        conn.commit()

        # Successful insertion
        return True

    # Return false upon duplicate username
    except sqlite3.IntegrityError:
        return False
    finally:  # Close the objects
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


def check_table(table: str) -> bool:
    """ check_table takes a string input representing a table name and checks if that table exists in
    'intranet_users.db'. """
    try:
        # Connect to database and establish a cursor
        conn = sqlite3.connect('db/intranet_users.db')
        cur = conn.cursor()

        # Query to see if table exists
        cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")

        # Return True or False if table exists
        if not cur.fetchone():
            return False
        return True

    # Print helpful error message upon unsuccessful completion
    except BaseException:
        print("ERROR: Could not connect to database")
    finally:  # Close the objects
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


insert_user_info("n", "n", AccessType.ADMIN)
