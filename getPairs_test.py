import unittest
from getPairs import getPairs


class GetStatsTest(unittest.TestCase):
    def test_get_stats_depth3(self):
        words = [
            'foo',
            'bar',
            'foo',
            'fish',
            'BAR',
            'Foo',
        ]
        res = [('foo', 'bar', 0), ('bar', 'foo', 0), ('foo', 'foo', 1), ('foo', 'foo', 1), ('foo', 'fish', 2),
               ('fish', 'foo', 2), ('bar', 'foo', 0), ('foo', 'bar', 0), ('bar', 'fish', 1), ('fish', 'bar', 1),
               ('bar', 'bar', 2), ('bar', 'bar', 2), ('foo', 'fish', 0), ('fish', 'foo', 0), ('foo', 'bar', 1),
               ('bar', 'foo', 1), ('foo', 'foo', 2), ('foo', 'foo', 2), ('fish', 'bar', 0), ('bar', 'fish', 0),
               ('fish', 'foo', 1), ('foo', 'fish', 1), ('bar', 'foo', 0), ('foo', 'bar', 0)]
        self.assertEqual(res, getPairs(words, 3))

    def test_get_stats_depth1(self):
        words = [
            'foo',
            'bar',
            'foo',
            'fish',
            'BAR',
            'Foo',
        ]
        res = [('foo', 'bar', 0), ('bar', 'foo', 0), ('bar', 'foo', 0), ('foo', 'bar', 0), ('foo', 'fish', 0),
               ('fish', 'foo', 0), ('fish', 'bar', 0), ('bar', 'fish', 0), ('bar', 'foo', 0), ('foo', 'bar', 0)]
        self.assertEqual(res, getPairs(words, 1))
