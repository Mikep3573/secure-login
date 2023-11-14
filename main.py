"""
Lab Assignment One
Michael Piscione
CS 2660 / Fall 2023

This is a simple login and menu for a pretend company's intranet system. The login requires users/employees
to enter a username and password in order to view a menu of options. A user's access level determines
whether they are allowed to click a menu option.
"""

import csv
import gen_functions

# Create dictionary for menu options and access levels
menu_options = {
    gen_functions.MenuOptions.EXIT: ["admin", "limited", "none"],
    gen_functions.MenuOptions.TIME_REPORTING: ["admin", "limited", "none"],
    gen_functions.MenuOptions.ACCOUNTING: ["admin", "limited"],
    gen_functions.MenuOptions.PRODUCT_PERFORMANCE: ["admin", "limited"],
    gen_functions.MenuOptions.PROJECTS: ["admin"],
    gen_functions.MenuOptions.EMPLOYEE_MANAGEMENT: ["admin"]
}

if __name__ == "__main__":
    # Check for file and open file
    try:
        with open("user_access_levels.csv", "r") as access_levels_file:
            # Create csv reader variable
            reader = csv.reader(access_levels_file)

            # Create a dictionary
            users = {}

            # Load the rows into the dictionary in the form -> user: [password, access level] and
            # Check for valid access levels in file
            row_counter = 0  # Initiate row counter
            error_rows = []  # Initiate a list of "error" rows
            for row in reader:
                row_counter += 1  # Increment row counter
                if row[2] != "admin" and row[2] != "limited" and row[2] != "none":
                    # If access level not recognized, add the number of the row to the list
                    error_rows.append(row_counter)
                else:
                    # If access level recognized, add the username, password, and access level to the dictionary
                    users[row[0]] = [row[1], row[2]]

            # If the list of error rows is not empty, print a formatted list of error rows and exit the program
            if len(error_rows) != 0:
                print("Access levels not recognized in rows:")
                print("-------------------------------------")
                for row in error_rows:  # Print the rows (numbers ascending, so the top row is one, then two, etc.)
                    print(row)
                print("-------------------------------------")
                print("Exiting now")
                exit()  # Exit the program

    except IOError:  # Print error message if unable to open file
        print("Could not read file")

    # Prompt for username and validate it
    username = gen_functions.prompt_username(users)

    # Prompt for password and validate it
    password = gen_functions.prompt_password(users, username)

    # Display menu
    gen_functions.display_menu()

    # Get user choice and validate it
    choice = gen_functions.menu_choice()

    # While choice not exit
    while choice != gen_functions.MenuOptions.EXIT:
        # Grab the user's access level
        access_level = users[username][1]

        # Check privileges
        if access_level not in menu_options[choice]:
            # Convert choice to something readable and
            # Display denial of access message
            print("You do not have access to {}".format(gen_functions.convert_user_choice(choice)))

        else:
            # Convert choice to something readable and
            # Display acceptance of access message
            print("Welcome to {}".format(gen_functions.convert_user_choice(choice)))

        # Ask the user if they want to see the menu and,
        # If so, get the choice and validate it
        choice = gen_functions.re_prompt_menu()

    # Print exiting message
    print("Goodbye!")
