import unittest
from os import remove
from time import time
from read import run
from db import add_words, connect_db, close_db, empty_table

file_name = 'temp_output_for_index_test.json'
file_name_csv = 'temp_output_for_index_test.csv'

db_name = 'testRead.sqlite'
table_name = 'test'

class ReadTest(unittest.TestCase):
    def setUp(self):
        # based on: "bear likes to fish twice"
        word_pairs = [
            ('bear', 'likes', 0),
            ('bear', 'to', 1),
            ('bear', 'fish', 2),
            ('likes', 'to', 0),
            ('likes', 'fish', 1),
            ('likes', 'twice', 2),
            ('to', 'fish', 0),
            ('to', 'twice', 1),
            ('fish', 'twice', 0),
        ]
        self.conn = connect_db(db_name, table_name)
        add_words(self.conn, word_pairs, table_name)

    def tearDown(self):
        empty_table(self.conn, table_name)
        close_db(self.conn)
        remove(db_name)

    def test_read_run(self):
        res = "WORD             ASSOC            DISTANCE         COUNT            \nlikes            to               0                1                \nlikes            fish             1                1                \nlikes            twice            2                1                \n"
        returned = run([
            '',
            'likes',
        ], db_name, table_name)
        self.maxDiff = None
        self.assertEqual(returned, res)

    def test_read_run_none(self):
        res = '\nThere are no results to show.\n'
        result = run([
            '',
            '9999',
        ], db_name, table_name)
        self.assertEqual(result, res)

    def test_read_all(self):
        res = "WORD             ASSOC            DISTANCE         COUNT            \n" \
            "bear             likes            0                1                \n" \
            "fish             twice            0                1                \n" \
            "likes            to               0                1                \n" \
            "to               fish             0                1                \n" \
            "bear             to               1                1                \n" \
            "likes            fish             1                1                \n" \
            "to               twice            1                1                \n" \
            "bear             fish             2                1                \n" \
            "likes            twice            2                1                \n"
        returned = run([
            '',
        ], db_name, table_name)
        self.maxDiff = None
        self.assertEqual(returned, res)



if __name__ == '__main__':
    unittest.main()

