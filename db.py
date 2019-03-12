import sqlite3
from sqlite3 import Error


def connect_db(db_file, table_name):
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    create_table(conn, table_name)
    return conn


def close_db(conn):
    conn.close()


def create_table(conn, table_name):
    try:
        c = conn.cursor()
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY, word text NOT NULL, word2 text NOT NULL, distance integer)"
        c.execute(sql)
        conn.commit()
    except Error as e:
        print(e)


def empty_table(conn, table_name):
    try:
        c = conn.cursor()
        sql = f"DELETE from {table_name}"
        c.execute(sql)
        conn.commit()
        return c.rowcount
    except Error as e:
        print(e)


def get_word(conn, word, table_name):
    cur = conn.cursor()
    cur.execute(f"SELECT word, word2, distance, COUNT(word) as word_count FROM {table_name} WHERE word = ? GROUP BY word, word2, distance ORDER BY distance ASC, word_count DESC", [word])
    result = cur.fetchall()
    # If nothing, return empty array
    if result is None:
        return []
    return result

def get_words(conn, table_name):
    cur = conn.cursor()
    cur.execute(f"SELECT word, word2, distance, COUNT(word) as word_count FROM {table_name} GROUP BY word, word2, distance ORDER BY distance ASC, word_count DESC")
    result = cur.fetchall()
    # If nothing, return empty array
    if result is None:
        return []
    return result


def add_words(conn, word_pairs, table_name):
    try:
        c = conn.cursor()
        c.executemany(f"INSERT INTO {table_name}(word, word2, distance) VALUES (?, ?, ?);", word_pairs)
        conn.commit()
        return c.rowcount
    except Error as e:
        print('Error adding:', e)