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
from os import urandom
import hashlib


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


def hash_pw(plain_text: str) -> str:
    """ TODO: Write this """
    # Generate a pseudorandom salt
    salt = urandom(20)  # Create a pseudorandom set of 20 bytes
    salt = salt.hex()  # 20 bytes converted into hex produces 40 characters
    hashable = salt + plain_text  # Concatenate salt and plain_text
    hashable = hashable.encode('utf-8')  # convert to bytes
    this_hash = hashlib.sha1(hashable).hexdigest()  # hash w/ SHA-1 and hex-digest

    # Prepend hash and return
    return salt + this_hash


def check_hashed(plain_text: str, salt: str, hashed: str) -> bool:
    """ TODO: Write this """
    # Hash salt + plain text
    hashable = salt + plain_text
    hashable = hashable.encode('utf-8')
    this_hash = hashlib.sha1(hashable).hexdigest()

    # Return True or False if stored hash equals new hash
    return this_hash == hashed[40:]


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
