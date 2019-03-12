import sys
from db import connect_db, close_db, get_word, get_words
from settings import settings
from format import formatToLines

def dealArgsRead(args):
    # first argument is the word
    if len(args) < 2:
        return {}
    return {
        'word': args[1],
    }

def run(args, db_name=settings['default_db'], table_name=settings['default_table']):
    options = dealArgsRead(args)
    conn = connect_db(db_name, table_name)
    rtn = ''
    if 'word' in options:
        counts = get_word(conn, options['word'], table_name)
    else:
        counts = get_words(conn, table_name)
    # Shut the database
    close_db(conn)
    # If no results
    if len(counts) == 0:
        rtn = '\nThere are no results to show.\n'
    # If there are results
    else:
        counts = [('WORD', 'ASSOC', 'DISTANCE', 'COUNT')] + counts
        lines = formatToLines(counts, 4)
        for line in lines:
            rtn += f'{line}\n'
    return rtn

if __name__ == '__main__':
    print(run(sys.argv))
