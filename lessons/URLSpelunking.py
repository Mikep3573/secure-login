"""
Lab Assignment Five
Michael Piscione
CS 2660 / Fall 2023

This performs URL 'spelunking' in the http://jreddy1.w3.uvm.edu/cs166/accounts/ directory. It uses a partial dictionary
to test many csv file names. If there are any csv's that have the form 'word from words_to_test.txt'.csv, it
creates a url using that filename. Once all words from words_to_test.txt have been checked. It attempts a GET
request using the different url's in the list. Once completed, the data retrieved from the urls are written to
separate files per individual url.

REFERENCES

Beautiful Soup documentation. Beautiful Soup Documentation - Beautiful Soup 4.12.0 documentation. (n.d.). https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 
Requests. PyPI. (n.d.). https://pypi.org/project/requests/ 
User guide Urllib3. urllib3. (n.d.). https://urllib3.readthedocs.io/en/stable/user-guide.html 
"""

from bs4 import BeautifulSoup
import urllib3
import requests

if __name__ == '__main__':
    # Open partial-dictionary file
    try:  # Attempt to open file
        with open('../instance/static/words_to_test.txt', 'r') as name_testing_file:
            # Read in the lines from the file
            lines = name_testing_file.readlines()

            # Make a list of urls to test
            test_urls = []

            # Iterate through each line, using the line to test for the name of the file
            # http://jreddy1.w3.uvm.edu/cs166/accounts/
            for line in lines:
                test_name = line.partition('\n')[0]  # Just the text, no \n
                url = 'http://jreddy1.w3.uvm.edu/cs166/accounts/' + test_name + '.csv'  # Create the test url
                request = requests.get(url)  # Get the request code
                if request.status_code == 200:  # If status code is 200, we found a file
                    test_urls.append(url)  # Add the url to the list

            # If file(s) was found
            if len(test_urls) > 0:
                # Get the data from the server
                # Set up a PoolManager object
                http = urllib3.PoolManager()

                # Create count variable for the loop
                count = 0

                # Test all urls
                for url in test_urls:
                    # Sending a GET request and getting back response as HTTPResponse object
                    response = http.request('GET', url)

                    # Get the data in the file (cast it to a string object)
                    response_data = str(BeautifulSoup(response.data, features="html.parser"))

                    # Attempt to write data to a file
                    try:
                        # Make a new file to write to (use count to differentiate the files)
                        with open('acc_data' + str(count) + '.csv', 'w') as acc_data_file:
                            # Replace all instances of \r, if there are any
                            if '\r' in response_data:
                                data = response_data.replace('\r', '')
                            else:
                                data = response_data

                            # Write the formatted data to the file in one shot
                            acc_data_file.write(data)
                    except Exception:
                        # Print message if we can't write the data to the file for any reason
                        print("Error writing data")
    except FileNotFoundError:
        # Print message if no file found with given name
        print("ERROR: No File Found")
