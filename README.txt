CS2660 Final Project
Project and README completed and written by Michael Piscione
----------------------------------------------------
Project Description:

The project employs a web front-end with the SQLite Python API database as part of the back-end. When a person first loads up the site, they are greeted with
a login page. This login page has a space for a username and password, and links to create an account or generate a random strong password. 
Upon entering your username and password, it will check if the username is available in the users table of the database and if the password (salted)
matches. A user is given three chances to login and can only do so after being locked out by either relaunching the Flask app or creating a new account
successfully. When a username and password is input, it checks if the password matches by taking the first 40 characters of the value stored for the password, 
prepends it to the inputted password and hashes that (using SHA-1). If the hashes match, the user is granted access to the intranet menu. 
A user's access type (none by default) determines which buttons appear. NONE: Exit and Time Reporting, LIMITED: Exit, Time Reporting, Accounting, and Projects, 
and ADMIN: Exit, Time Reporting, Accounting, Projects, Product Performance, and Employee Management. Upon clicking these buttons the website 
displays a simple WELCOME message (unless they click Exit, which brings them back to the main menu). 
The security functionality required and available for this design include the prevention of XSS and SQL injection (among others).
If the user decides to create a new account they first need to create a unique username (one that does not already exist in the database) and a password that
follows the project description for a password. If either of these do not occur, the user is given an appropriate message. If a user registers successfully,
they get a message saying so. This (as described earlier), resets their failed login attempt counter.

Database Setup:

Database setup should be pretty simple, just make sure there is a directory called db in the project root directory. main.py should create the
database in that directory if it does not exist already (same goes for the 'users' table). The database should have a table called 'users' with 'username',
'password', and 'access_type' as the column headers (note that 'username' is UNIQUE). 

There is currently no way of creating an account to have any other access type other than NONE (using the website), so in database_funcs.py simply call insert_user_info with
your chosen username, password, and AccessType (found in classes/access_types.py). Note that the project description's required password format does not apply here.

Running Project:

Once setup is done (testing instructions are completed), you should simply have to click run in main.py. From here, you can use the hyperlink provided
by Flask or got to http://localhost:8097 to find the website. The first page you should see is at '/' (rendering index.html).

Testing:

1.) I ran this whole project in PyCharm and the website on Google Chrome. I would recommend using Chrome, if possible, as I am working with fonts.googleapis.com
which works differently for different browsers. Note that this is only for the "Share Tech" font. Your IDE should not be an issue but I thought I'd list
what I used here.
2.) I used Python 3.11 but Python 3.9 and above may still work
3.) You should have the latest version of sqlite3, random, urandom (from os), hashlib, traceback, app, and flask (specifically, Flask, render_template, request, and redirect) downloaded.
	3a.) Note that some of these may not even be needed to be downloaded and should already come in Python's extended library.
4.) File Structure: in project root: directories: classes, db, static, templates, files: app.py, database_funcs.py, gen_functions.py, main.py, and README.txt.
	4a.) classes should have access_types.py. db should have intranet_users.db (this doesn't necessarily need to be there to start, one is automatically created
	in db if it is not available, same goes for the 'users' table). This database should have a table called 'users' after main.py is run. static should have style.css and
	wave.jpg. templates should have accepted_choice.html, index.html, intranet_menu.html, and register.html.
5.) I would create three users (using insert_user_info in database_funcs.py) that have AccessType.NONE, AccessType.LIMITED, and AccessType.ADMIN to test the full suite of
'intranet_menu.html' buttons.
6.) Make sure you are able to execute SQLite commands to the database

This should be about it for testing, if there is any issues, please don't hesitate to reach out to Michael.Piscione@uvm.edu or mpiscion@uvm.edu

References:
(I couldn't cite many of these using APA citations, I hope this suffices)

I used some of Professor Eddy's Bank app (and other code) to create this. This includes the SQLite demo for creating and storing information in the database and the
html and css as a reference.

I also reused some of my previous code from past labs for some of the security functionality.

wave.jpg came from user TsMax88 on r/WQHD_Wallpaper - reddit:
https://www.reddit.com/r/WQHD_Wallpaper/comments/15hgoml/waves_at_dawn_5160x2160/

CSS Reference (w3schools.com):
CSS reference. (n.d.-a). https://www.w3schools.com/cssref/index.php 

HTML Reference (w3schools.com):
HTML element reference. HTML Reference. (n.d.). https://www.w3schools.com/tags/default.asp 

SQL Reference (w3schools.com):
SQL tutorial. (n.d.). https://www.w3schools.com/sql/ 

SQLite API Reference (docs.python.org):
SQLITE3 - DB-API 2.0 interface for SQLite databases. 
	Python documentation. (n.d.). https://docs.python.org/3/library/sqlite3.html 

SQLite Reference (sqlite.org):
Sqlite Home Page. (n.d.). https://www.sqlite.org/index.html 

Baseline for website style came from:
YouTube video by Codehal. This helped a lot in creating a baseline for the style of the website. 
YouTube. (2023). Login Form in HTML &amp; CSS. YouTube. Retrieved November 22, 2023, 
	from https://www.youtube.com/watch?v=hlwlM4a5rxg&amp;ab_channel=Codehal. 