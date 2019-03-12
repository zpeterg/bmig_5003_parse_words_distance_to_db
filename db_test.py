import unittest
from db import add_words, close_db, connect_db, empty_table, get_word, get_words
from os import remove

db_name = 'test.sqlite'
table_name = 'test'

class dbTest(unittest.TestCase):
    def tearDown(self):
        conn = connect_db(db_name, table_name)
        close_db(conn)
        remove(db_name)

    def test_create_table(self):
        conn = connect_db(db_name, table_name)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_list = cur.fetchall()
        close_db(conn)
        self.assertEqual(table_list[0][0], table_name)

    def test_add_words(self):
        word_pairs = [
            ('fish', 'hook', 1),
            ('bear', 'trap', 2),
            ('person', 'creditcard', 3),
        ]
        conn = connect_db(db_name, table_name)
        result_modified = add_words(conn, word_pairs, table_name)
        # make a new connection to make sure changes have been persisted
        conn2 = connect_db(db_name, table_name)
        cur = conn2.cursor()
        cur.execute(f"SELECT word, word2, distance FROM {table_name}")
        result = cur.fetchall()
        close_db(conn2)
        self.assertEqual(result, word_pairs)
        self.assertEqual(result_modified, 3)

    def test_empty_table(self):
        word_pairs = [
            ('fish', 'hook', 1),
            ('bear', 'trap', 2),
            ('person', 'creditcard', 3),
        ]
        conn = connect_db(db_name, table_name)
        add_words(conn, word_pairs, table_name)
        # testing this
        empty_table(conn, table_name)

        cur = conn.cursor()
        cur.execute(f"SELECT word, word2, distance FROM {table_name}")
        result = cur.fetchall()
        close_db(conn)
        self.assertEqual(result, [])

    def test_get_word(self):
        word_pairs = [
            ('fish', 'fire', 0),
            ('fish', 'hook', 0),
            ('fish', 'hook', 1),
            ('fish', 'hook', 1),
            ('bear', 'trap', 2),
            ('creditcard', 'person', 3),
            ('person', 'creditcard', 3),
            ('person', 'creditcard', 3),
        ]
        conn = connect_db(db_name, table_name)
        add_words(conn, word_pairs, table_name)
        # testing this
        response = get_word(conn, 'fish', table_name)
        self.assertEqual(response, [
            ('fish', 'fire', 0, 1),
            ('fish', 'hook', 0, 1),
            ('fish', 'hook', 1, 2),
        ])

    def test_get_words(self):
        word_pairs = [
            ('fish', 'hook', 1),
            ('fish', 'hook', 1),
            ('bear', 'trap', 2),
            ('creditcard', 'person', 3),
            ('person', 'creditcard', 3),
            ('person', 'creditcard', 3),
        ]
        res = [
            ('fish', 'hook', 1, 2),
            ('bear', 'trap', 2, 1),
            ('person', 'creditcard', 3, 2),
            ('creditcard', 'person', 3, 1),
        ]
        conn = connect_db(db_name, table_name)
        add_words(conn, word_pairs, table_name)
        # testing this
        response = get_words(conn, table_name)
        self.assertEqual(response, res)


