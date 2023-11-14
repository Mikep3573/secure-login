"""
Lab Assignment Six
Michael Piscione
CS 2660 / Fall 2023

This file is for PART II of Lab Asssignment Six. It takes a partial-dictionary and hashes the words presented in
the file. It then compares these hashes against the hashed passwords in the passwd file to check which match.
Given a match, it writes the plaintext password along with the corresponding username to a file entitled
unencrypted_passwords.

REFERENCES

Hashlib - secure hashes and message digests. Python documentation. (n.d.).
    https://docs.python.org/3/library/hashlib.html

"""

# Import dependencies
import hashlib

# Run the program
if __name__ == '__main__':
    # Read in wordlist file
    try:
        with open('../instance/static/wordlist.txt', 'r') as words_file:
            # Create a dictionary to store word/encrypted word pairs
            encrypted_words_dict = {}

            # Iterate through all the words in the file
            for word in words_file:
                # Remove the trailing newline character
                word = word.strip('\n')

                # Encode the formatted word as type: bytes
                encoded_word = word.encode('utf-8')

                # Pass formatted word through SHA-1 algorithm
                # and add it as a value into the dictionary using the unencrypted word as its key
                encrypted_words_dict[word] = hashlib.sha1(encoded_word).hexdigest()

    # Print helpful message if file wasn't found
    except FileNotFoundError:
        print('ERROR: Wordlist file not found')

    # Read in passwd file
    try:
        with open('../instance/static/passwd', 'r') as acc_info_file:
            # Ignore the header row and place the rest of the lines into a list
            lines = acc_info_file.readlines()[1:]

            # Create a dictionary object to hold encrypted passwords and usernames
            passwords_dict = {}

            # Iterate through every line (except the header)
            for line in lines:
                # Grab the encrypted password in each line and insert it into the dictionary
                # as a key and the username as the value
                line = line.strip('\n').split(sep=',')
                passwords_dict[line[2]] = line[0]

    # Print helpful message if file wasn't found
    except FileNotFoundError:
        print('ERROR: Account Info file not found')

    # Output found passwords to a file
    # NOTE: I added usernames just for ease of use
    try:
        # Open a new file to write to
        with open('../instance/static/unencrypted_passwords.txt', 'w') as unencrypted_passwords_file:
            # Iterate through every hashed word and see if it matches a hashed password
            for key in encrypted_words_dict:
                if encrypted_words_dict[key] in passwords_dict.keys():
                    # If a hashed word matches a hashed password, write the unencrypted word
                    # and its corresponding username to a file
                    unencrypted_passwords_file.write(passwords_dict[encrypted_words_dict[key]] + ': ' + key + '\n')

    # If bad file name, print helpful message
    except FileNotFoundError:
        print('ERROR: Unecrypted Passwords file not found')
