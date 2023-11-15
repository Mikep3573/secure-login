# Lab Assignment One
### CS 2660
### Michael Piscione

-------------------------
### Description
This program represents Lab Assignment One. It was completed on September 9th, 2023 by Michael Piscione.

The data does not represent anyone's real usernames or passwords. It is fictional.

The data (usernames, passwords, and access levels) are stored in a csv called user_access_levels.csv. There are fourteen
rows each consisting of a username, a password, and the access level for one user. 

main.py starts by using the csv python library to read in the data from the file, once the file has been validated. 
If there is an error in the access levels (i.e., misspelling) it will throw an error and tell you which row(s) the 
error occurred. Otherwise, the program will continue by moving into the login screen. Furthermore, the data is loaded
into a dictionary with the usernames as the keys pointing to lists containing the password and access level for each 
user. 

The program first prompts the user for their username. Once validated, the program prompts the user for their password. 
If the password matches the password stored for that user, the program will show the user the menu. The program does 
not allow access to the menu if the user does not either provide a valid username or the correct password for that 
username.

Once the user has logged in, the program will present them with a choice of options:

0: Exit, 1: Time Reporting, 2: Accounting, 3: Product Performance, 4: Projects, and 5: Employee Management.

The user takes an input (string 0-5). The program validates the user's input as being one of the menu options. 
It does not allow the user to continue if a valid input is not given.

Once the string has been validated, the choice's corresponding user access levels (i.e., the list of possible
access levels of users that can view it) is compared to the user's access level. If the user's access level is present
in the choice's corresponding access levels, the user will get a message welcoming them to that part of the menu.
Otherwise, the user will get a notification telling them that they do not have access to that part of the menu.

After the corresponding message is given, the program prompts the user for a choice of seeing the menu again or exiting. 
The program validates this input as well (either 'Y' or 'y' for seeing the menu or 'N' or 'n' for exiting the program).
Upon responding with 'N' or 'n', the program will end with a closing message. If the user chooses to see the menu again, 
the whole process starts over ("Once the user has logged in..." and down). If the user provides neither, the program
will re-prompt until a valid input is given.

This project also contains gen_functions.py which contains:

-A class (MenuOptions), containing global constants to be used both in the supplemental gen_functions.py file
and main.py.

-All-purpose functions used for things like gathering user input, presenting the menu to the user, and converting
the user's string 0-5 input to a readable menu option (i.e., 'Accounting', 'Projects', etc).

-------------------------
### Testing

NOTE: There is no dedicated testing file for the program (not in lab specification).

NOTE: I used python 3.10

NOTE: I used the csv python library. I doubt you'll need to download it but just know you might.

#### List of items to test (not necessarily in this order):

1: File name validation

2: Access level validation

3: Username validation

4: Password validation and log-in accuracy

5: Menu pop-up (does it pop-up)

6: Menu choice validation

7: 'See menu again' choice validation

8: Can someone with the correct access level access all items associated with that level (and vice versa)

#### Item Descriptions:

1: Try editing the name of the file/removing the file from the folder. Does the error message/exception message pop-up?

2: Try editing the names of one or more of the access levels directly in the file. Will the program catch the change
and will it show the rows that were changed accurately?

3: If you enter a username not in the file, will it catch it and re-prompt you always? Similarly, will it always 
recognize the usernames present in the file?

4: Similar to item three. If you enter a password not on file for someone, will it catch it and re-prompt you always? 
Similarly, will it always recognize the password present in the file?

5: Does the menu show up upon correct username/password?

6: Will the program re-prompt you/allow you to continue given a choice not 0-5?

7: Will the program re-prompt you/allow you to continue given a choice in the 'See menu again?' screen that is
not 'Y', 'y', 'N', or 'n'? Try checking vice versa for this as well.

8: This should be self-explanatory.

