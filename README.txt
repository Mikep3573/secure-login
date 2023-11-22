CS2660 Final Project
Project and README completed and written by Michael Piscione
----------------------------------------------------
Project Description:

The project employs a web front-end with the SQLite Python API as part of the back-end. When a person first loads up the site, they are greeted with
a login page. This login page has a space for a username, password, and links to create an account or generate a random strong password. 
Upon entering your username and password, it will check if the username is available in the users table of the database and if the password (salted)
matches. A user is given three chances to login and can only do so afterwards by either relaunching the Flask app or creating a new account
successfully. It checks if the password matches by taking the first 40 characters of the value stored for the password, prepends it to the inputted password
and hashes that (using SHA-1). If the hashes match, the user is granted access to the intranet menu. A user's access type (none by default) determines which buttons
appear. NONE: Exit and Time Reporting, LIMITED: Exit, Time Reporting, Accounting, and Projects, and ADMIN: Exit, Time Reporting, Accounting, Projects, Product
Performance, and Employee Management. Upon clicking these buttons the website displays a simple WELCOME message (unless they click Exit, which brings
them back to the main menu). The security functionality required and available for this design include the prevention of XSS and SQL injection (among others).
If the user decides to create a new account they first need to create a unique username (one that does not already exist in the database) and a password that
follows the project description for a password. If either of these do not occur, the user is given an appropriate message. If a user registers successfully,
they get a message saying so. This (as described earlier), resets their failed login attempt counter.


Database Setup:

Running Project:

Testing:

References: