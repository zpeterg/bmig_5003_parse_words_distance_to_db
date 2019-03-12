import unittest
from os import remove
from time import time
from index import getAndFilter, run
from db import connect_db, close_db, empty_table

file_name = 'temp_output_for_index_test.json'
file_name_csv = 'temp_output_for_index_test.csv'

db_name = 'test.sqlite'
table_name = 'test'

class IndexTest(unittest.TestCase):
    def tearDown(self):
        conn = connect_db(db_name, table_name)
        empty_table(conn, table_name)
        close_db(conn)
        remove(db_name)

    # def test_speed_with_moby(self):
    #     t0 = time()
    #     options = {
    #         'files': ['moby_test.txt'],
    #         'start': 'whale',
    #         'stop': 'mast',
    #         'finish': 'ffff9999',
    #     }
    #     self.assertLess(190000, len(getAndFilter(options)))
    #     t1 = time()
    #     print('Moby total get & parse time sec:', t1 - t0)


    def test_get_and_filter_simple(self):
        options = {
            'files': ['testfiles/small_test.txt'],
            'start': 'foo',
            'stop': 'bar',
            'finish': 'enough',
        }
        res = [
            'cow',
            'cow',
            'siamese',
            'wonderland',
            'foo',
            'toothpaste',
            'milky',
            'flight-manual',
            'toothpick',
        ]
        self.assertEqual(getAndFilter(options), res)


    def test_index_run(self):
        res = [('cow', 'cow', 0), ('cow', 'cow', 0), ('cow', 'siamese', 1), ('siamese', 'cow', 1),
               ('cow', 'wonderland', 2), ('wonderland', 'cow', 2), ('cow', 'foo', 3), ('foo', 'cow', 3),
               ('cow', 'siamese', 0), ('siamese', 'cow', 0), ('cow', 'wonderland', 1), ('wonderland', 'cow', 1),
               ('cow', 'foo', 2), ('foo', 'cow', 2), ('cow', 'toothpaste', 3), ('toothpaste', 'cow', 3),
               ('siamese', 'wonderland', 0), ('wonderland', 'siamese', 0), ('siamese', 'foo', 1), ('foo', 'siamese', 1),
               ('siamese', 'toothpaste', 2), ('toothpaste', 'siamese', 2), ('siamese', 'milky', 3),
               ('milky', 'siamese', 3), ('wonderland', 'foo', 0), ('foo', 'wonderland', 0),
               ('wonderland', 'toothpaste', 1), ('toothpaste', 'wonderland', 1), ('wonderland', 'milky', 2),
               ('milky', 'wonderland', 2), ('wonderland', 'flight-manual', 3), ('flight-manual', 'wonderland', 3),
               ('foo', 'toothpaste', 0), ('toothpaste', 'foo', 0), ('foo', 'milky', 1), ('milky', 'foo', 1),
               ('foo', 'flight-manual', 2), ('flight-manual', 'foo', 2), ('foo', 'toothpick', 3),
               ('toothpick', 'foo', 3), ('toothpaste', 'milky', 0), ('milky', 'toothpaste', 0),
               ('toothpaste', 'flight-manual', 1), ('flight-manual', 'toothpaste', 1), ('toothpaste', 'toothpick', 2),
               ('toothpick', 'toothpaste', 2), ('milky', 'flight-manual', 0), ('flight-manual', 'milky', 0),
               ('milky', 'toothpick', 1), ('toothpick', 'milky', 1), ('flight-manual', 'toothpick', 0),
               ('toothpick', 'flight-manual', 0)]
        run([
            '',
            '--input=testfiles/small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
            '-c',
        ], db_name, table_name)
        conn = connect_db(db_name, table_name)
        cur = conn.cursor()
        cur.execute(f"SELECT word, word2, distance FROM {table_name}")
        result = cur.fetchall()
        close_db(conn)
        self.assertEqual(result, res)


    def test_index_run_twice(self):
        res = [
            ('cow', 'cow', 0), ('cow', 'cow', 0), ('cow', 'siamese', 1), ('siamese', 'cow', 1),
            ('cow', 'wonderland', 2), ('wonderland', 'cow', 2), ('cow', 'foo', 3), ('foo', 'cow', 3),
            ('cow', 'siamese', 0), ('siamese', 'cow', 0), ('cow', 'wonderland', 1), ('wonderland', 'cow', 1),
            ('cow', 'foo', 2), ('foo', 'cow', 2), ('cow', 'toothpaste', 3), ('toothpaste', 'cow', 3),
            ('siamese', 'wonderland', 0), ('wonderland', 'siamese', 0), ('siamese', 'foo', 1), ('foo', 'siamese', 1),
            ('siamese', 'toothpaste', 2), ('toothpaste', 'siamese', 2), ('siamese', 'milky', 3),
            ('milky', 'siamese', 3), ('wonderland', 'foo', 0), ('foo', 'wonderland', 0),
            ('wonderland', 'toothpaste', 1), ('toothpaste', 'wonderland', 1), ('wonderland', 'milky', 2),
            ('milky', 'wonderland', 2), ('wonderland', 'flight-manual', 3), ('flight-manual', 'wonderland', 3),
            ('foo', 'toothpaste', 0), ('toothpaste', 'foo', 0), ('foo', 'milky', 1), ('milky', 'foo', 1),
            ('foo', 'flight-manual', 2), ('flight-manual', 'foo', 2), ('foo', 'toothpick', 3),
            ('toothpick', 'foo', 3), ('toothpaste', 'milky', 0), ('milky', 'toothpaste', 0),
            ('toothpaste', 'flight-manual', 1), ('flight-manual', 'toothpaste', 1), ('toothpaste', 'toothpick', 2),
            ('toothpick', 'toothpaste', 2), ('milky', 'flight-manual', 0), ('flight-manual', 'milky', 0),
            ('milky', 'toothpick', 1), ('toothpick', 'milky', 1), ('flight-manual', 'toothpick', 0),
            ('toothpick', 'flight-manual', 0),
            ('cow', 'cow', 0), ('cow', 'cow', 0), ('cow', 'siamese', 1), ('siamese', 'cow', 1),
            ('cow', 'wonderland', 2), ('wonderland', 'cow', 2), ('cow', 'foo', 3), ('foo', 'cow', 3),
            ('cow', 'siamese', 0), ('siamese', 'cow', 0), ('cow', 'wonderland', 1), ('wonderland', 'cow', 1),
            ('cow', 'foo', 2), ('foo', 'cow', 2), ('cow', 'toothpaste', 3), ('toothpaste', 'cow', 3),
            ('siamese', 'wonderland', 0), ('wonderland', 'siamese', 0), ('siamese', 'foo', 1), ('foo', 'siamese', 1),
            ('siamese', 'toothpaste', 2), ('toothpaste', 'siamese', 2), ('siamese', 'milky', 3),
            ('milky', 'siamese', 3), ('wonderland', 'foo', 0), ('foo', 'wonderland', 0),
            ('wonderland', 'toothpaste', 1), ('toothpaste', 'wonderland', 1), ('wonderland', 'milky', 2),
            ('milky', 'wonderland', 2), ('wonderland', 'flight-manual', 3), ('flight-manual', 'wonderland', 3),
            ('foo', 'toothpaste', 0), ('toothpaste', 'foo', 0), ('foo', 'milky', 1), ('milky', 'foo', 1),
            ('foo', 'flight-manual', 2), ('flight-manual', 'foo', 2), ('foo', 'toothpick', 3),
            ('toothpick', 'foo', 3), ('toothpaste', 'milky', 0), ('milky', 'toothpaste', 0),
            ('toothpaste', 'flight-manual', 1), ('flight-manual', 'toothpaste', 1), ('toothpaste', 'toothpick', 2),
            ('toothpick', 'toothpaste', 2), ('milky', 'flight-manual', 0), ('flight-manual', 'milky', 0),
            ('milky', 'toothpick', 1), ('toothpick', 'milky', 1), ('flight-manual', 'toothpick', 0),
            ('toothpick', 'flight-manual', 0)
        ]
        run([
            '',
            '--input=testfiles/small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
        ], db_name, table_name)
        # run a second time
        run([
            '',
            '--input=testfiles/small_test.txt',
            '--start=foo',
            '--stop=bar',
            '--finish=007',
        ], db_name, table_name)
        conn = connect_db(db_name, table_name)
        cur = conn.cursor()
        cur.execute(f"SELECT word, word2, distance FROM {table_name}")
        result = cur.fetchall()
        close_db(conn)
        self.assertEqual(result, res)


if __name__ == '__main__':
    unittest.main()

