import sys
from getFile import getFile
from filter import Filter
from utils import dealArgs
from getPairs import getPairs
from db import connect_db, close_db, add_words, empty_table

def getAndFilter(options):
    """
    Retrieves the files listed within options['files'] and filters them based on the other options[...]
    Returns array of cleaned, filtered words.
    """
    # Create the Filter class
    f = Filter(options)
    rtn = []
    for file in options['files']:
        # Get the words, passing-in the callback filter()
        rtn += getFile(file, f.filter)
    return rtn

def run(args, db_name='main.sqlite', table_name='main'):
    """
    Takes arguments (usually from command-line), parses them, and retrieves the words, filters, and formats them.
    Returns a formatted string ready to print-to-screen.
    """
    rtn = ''
    # Parse the arguments
    options = dealArgs(args).to_object()
    # Get and filter the words
    words = getAndFilter(options)
    word_pairs = getPairs(words)
    conn = connect_db(db_name, table_name)
    # If -c argument passed, clear out the table
    if options['clear']:
        removed_rows = empty_table(conn, table_name)
        rtn += f'\nRemoved {removed_rows} rows.'
    # Add the word-pairs & get the count
    modified_rows = add_words(conn, word_pairs, table_name)
    # Close the database
    close_db(conn)
    # If nothing saved, give a warning
    if modified_rows <= 0:
        rtn += f'\nFailed to save anything'
    # If something saved, state the count
    else:
        rtn += f'\nSuccessfully added {modified_rows} words'
    return rtn

if __name__ == '__main__':
    print(run(sys.argv))
