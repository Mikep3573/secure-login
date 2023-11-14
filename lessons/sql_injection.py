""""
SQL Injection Example
This function is the only one you are permitted
to modify for the lab assignment.

Note: if you aren't familiar with str.format, here
is a link to the docs:
https://docs.python.org/3/library/stdtypes.html#str.format
"""


def create_search_query(account_id: int, search_term: str) -> str:
    """
    Creation of SQL query that has injection vulnerability.
    You should be able to
        1) explain why this is vulnerable,
        2) demonstrate how to exploit this vulnerability, and
        3) modify this code to prevent SQL injection attack
    :param account_id: int
    :param search_term: str
    :return: str (the query)
    """
    # ------ MY CODE ------
    # Filter search_term to be only the item that appears before %"
    # A search_term that ends the substring specification early is probably an SQL injection
    search_term = search_term.partition('%"')[0]
    # ^ This allows for valid search terms before preemptively ending the substring

    # In the event '%"' not in search_term, SQL injection can still occur by starting the string with "
    # Removing instances of " seems to allow sql injections to go through without actually executing the code
    # Furthermore, removing " seems to reduce the possibility of invalid syntax error happening and
    # any searches that legitimately involve " should all still work granted there's alphabetic characters as well
    search_term = search_term.replace('"', "")

    # ------ CODE GIVEN ------
    q = 'SELECT * FROM trnsaction ' \
        'WHERE trnsaction.account_id = {} ' \
        'AND ' \
        'trnsaction.memo LIKE "%{}%"'.format(account_id, search_term)
    return q


create_search_query(1234, '"')
