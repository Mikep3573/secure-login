"""
General Functions
Michael Piscione
CS 2660/Fall 2023

gen_functions.py is a supplemental file used to store functions used throughout the project.
Functions consist of checking password requirements and hashing passwords (among others).
"""

# Dependencies
from classes.access_types import *
from random import *
from os import urandom
import hashlib


def create_password() -> str:
    """ create_password randomly generates a password according to the password specifications (can be seen in
    check_password). It does this by randomly selecting characters from a list of all possible characters. If
    the requirements are NOT met, a new password is created until they are. The 'strong' password is returned. """
    # Create a return string
    return_string = ''

    # Decide length
    length = randint(8, 25)

    # Create a string variable for all possible characters in a password
    all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?-+[]{};:'",./\\?><|`~"

    # Create a temporary random password
    temp_pass = return_string.join(choice(all_chars) for i in range(length))

    # Continuously create a new password and check if it meets requirements
    # Stop when it does
    while not check_password(temp_pass):
        return_string = ''  # Reset return_string
        temp_pass = return_string.join(choice(all_chars) for i in range(length))

    # Return the generated password
    return temp_pass


def check_password(password: str) -> bool:
    """ check_password tests if a password has 25 >= length >= 8, at least one number, at least one lowercase letter,
     at least one uppercase letter, and at least one special character. Returns True or False accordingly. """
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
    """ hash_pw takes a plain text password, generates a pseudorandom salt of 40 hex characters, hashes
    salt + plain_text, and returns salt + hashed. """
    # Generate a pseudorandom salt
    salt = urandom(20)  # Create a pseudorandom set of 20 bytes
    salt = salt.hex()  # 20 bytes converted into hex produces 40 characters
    hashable = salt + plain_text  # Concatenate salt and plain_text
    hashable = hashable.encode('utf-8')  # Convert to bytes
    this_hash = hashlib.sha1(hashable).hexdigest()  # Hash w/ SHA-1 and hex-digest

    # Prepend salt and return
    return salt + this_hash


def check_hashed(plain_text: str, salt: str, hashed: str) -> bool:
    """ check_hashed takes a plain text password, a salt, and a hashed password (with the same salt prepended).
     It hashes salt + plain_text and checks if the hashed password (every character after the first forty)
     match. """
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
