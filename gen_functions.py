"""
General Functions
Michael Piscione
CS 2660/Fall 2023

gen_functions.py is a supplemental file used to store functions and constants used throughout the lab.
I stored the menu choices as constants in this file as well as functions used in getting user input and displaying
the menu.
"""

# Dependencies
from classes.access_types import *
from random import *


def create_password() -> str:
    """ TODO: Write this """
    # Create a return string
    return_string = ''

    # Decide length
    length = randint(8, 25)

    # Create a string variable for all possible characters in the password
    all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?-+[]{};:'",./\\?><|`~"

    # Create a temporary random password
    temp_pass = return_string.join(choice(all_chars) for i in range(length))

    # Continuously check if temp_pass meets requirements
    while not check_password(temp_pass):
        return_string = ''
        temp_pass = return_string.join(choice(all_chars) for i in range(length))

    # Return the generated password
    return temp_pass


def check_password(password: str) -> bool:
    """ TODO: Write this """
    # Create boolean flags for all password conditions
    length = False
    num = False
    lower = False
    upper = False
    special = False

    # Check length condition
    if 25 >= len(password) >= 8:
        length = True

    # Check other conditions
    for char in password:
        if char.isnumeric():  # numeric character
            num = True
        elif char.isupper():  # uppercase character
            upper = True
        elif char.islower():  # lowercase character
            lower = True
        elif not char.isalnum():  # Not alphanumeric (is special)
            special = True

    # If all tests pass, return True, False otherwise
    if length and num and lower and upper and special:
        return True
    return False


def convert_access_type(access_type: str) -> AccessType:
    """ convert_access_type takes a string access type and converts it to an AccessType constant. """

    # Match the string access type to an AccessType
    match access_type:
        case "admin":
            return AccessType.ADMIN
        case "limited":
            return AccessType.LIMITED
        case "none":
            return AccessType.NONE

    # Return NULL type if none found
    return AccessType.NULL