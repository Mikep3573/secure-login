"""
General Functions
Michael Piscione
CS 2660/Fall 2023

gen_functions.py is a supplemental file used to store functions and constants used throughout the lab.
I stored the menu choices as constants in this file as well as functions used in getting user input and displaying
the menu.
"""

# Dependencies
from classes.options import *
from classes.access_types import *


def prompt_username(users):
    """ Prompts and collects user input as their username. Takes parameter 'users', a dictionary, to validate
    the username (whether it's in the dictionary as a key). If it is not a key, it continuously re-prompts
    the user until a username is entered that is a key. Returns the validated username (string). """

    username = input("Please enter your username: ")  # Get initial user input

    while username not in users:  # Check for validity
        print("Invalid username")  # Give error message if username not valid
        username = input("Please re-enter username: ")  # Re-prompt if username not valid

    return username  # Return validated input


def prompt_password(users, username):
    """ Prompts and collects user input as their password. Takes parameter 'users', a dictionary, to validate
    the password using the other parameter 'username', a string, as a key. The keys point to a list of two items.
    One of them is the password, the other is the access level associated with the username.
    The function compares the user's input against the password stored. If the user's input is not the same as the
    stored password, the user is continuously re-prompted until a valid password is entered.
    Returns the validated password (string). """

    password = input("Please enter your password: ")  # Get initial user input

    while password != users[username][0]:  # Check for validity
        print("Invalid password")  # Give error message if password not valid
        password = input("Please re-enter password: ")  # Re-prompt if password not valid

    return password  # Return validated input


def menu_choice():
    """ Prompts user for a menu option (given as a number 0-5 as a string). Takes no parameters.
    Compares the string given against all possible inputs. If the input does not match a valid choice,
    the function continuously re-prompts until a valid choice is given.
    Returns the valid choice (still a number 0-5 as a string). """

    choice = input("Please enter an option number: ")  # Get initial user input

    # Check for validity
    while choice != MenuOption.EXIT and choice != MenuOption.TIME_REPORTING and \
            choice != MenuOption.ACCOUNTING and choice != MenuOption.PRODUCT_PERFORMANCE and \
            choice != MenuOption.PROJECTS and choice != MenuOption.EMPLOYEE_MANAGEMENT:
        print("Not valid choice")  # Give error message if choice not valid
        choice = input("Please re-enter an option number: ")  # Re-prompt if choice not valid

    return choice  # Return validated input


def display_menu():
    """ Displays a formatted menu of options. This is the menu shown after a user successfully logs in. Takes no
    parameters and returns nothing. """

    # Print the formatted menu
    print("-----------MENU-----------")
    print("0: Exit")
    print("1: Time Reporting")
    print("2: Accounting")
    print("3: Product Performance")
    print("4: Projects")
    print("5: Employee Management")
    print("--------------------------")


def re_prompt_menu():
    """ Prompts the user for a choice of whether to the show the menu again or quit the program. Takes no parameters.
    Validates the user input as either being 'Y' or 'y' for 'Yes, I would like to see the menu again', or 'N' or 'n' for
    'No, I would not like to see the menu again'. Continuously re-prompts for a valid choice of yes or no. If the user
    wants the menu again the function calls both display_menu and menu_choice. Both of these
    have their own docstrings, but it essentially displays the menu and returns a validated menu option given by
    the user (respectively). The function returns a valid menu option or EXIT/'0' if they don't want the menu again. """

    # Ask if they would like the menu again
    user_menu_choice = input("Would you like to make another choice? (Y/N): ")

    # While the choice is an invalid option, re-prompt
    while user_menu_choice != "Y" and user_menu_choice != "y" and user_menu_choice != "N" and user_menu_choice != "n":
        print("Invalid choice")  # Give error message if invalid choice
        user_menu_choice = input("Please enter Y or N (not case sensitive): ")  # Re-prompt for valid choice

    # Display menu and return validated user choice if answer was yes
    if user_menu_choice == "Y" or user_menu_choice == "y":
        display_menu()
        return menu_choice()

    # Exit the program if answer was no
    else:
        return MenuOption.EXIT


def convert_user_choice(choice):
    """ Converts the user's choice (number 0-5 as string) to an english menu option. Used for printing the user's choice
     as a word not a string number. Takes parameter 'choice', a string, for conversion.
     Returns the english menu option. """

    # Match numerical choice to the english version of it
    # Return the english word
    match choice:
        case MenuOption.EXIT:
            return "exit"
        case MenuOption.TIME_REPORTING:
            return "time reporting"
        case MenuOption.ACCOUNTING:
            return "accounting"
        case MenuOption.PRODUCT_PERFORMANCE:
            return "product performance"
        case MenuOption.PROJECTS:
            return "projects"
        case MenuOption.EMPLOYEE_MANAGEMENT:
            return "employee management"


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
