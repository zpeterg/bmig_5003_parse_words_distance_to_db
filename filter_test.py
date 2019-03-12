import unittest
from filter import Filter

options = {'start': 'foo', 'stop': 'Bar', 'finish': 'enough'}
words = [
    'fish',
    'hat',
    'Foo',
    'cow',
    'SIAMESE',
    'wonderland##',
    'FOO',
    'toothpaste',
    'bar',
    'umbrella',
    'foo##',
    'milky',
    'flight-manual',
    'toothpick',
    'bar',
    'enough',
    'event-horizon',
    'bar'
]

class FilterTest(unittest.TestCase):
    def test_constructor(self):
        w = Filter(options)
        self.assertEqual(w.start, options['start'].lower())
        self.assertEqual(w.stop, options['stop'].lower())
        self.assertEqual(w.finish, options['finish'].lower())

    def test_filter_simple(self):
        res = [
            '',
            '',
            '',
            'cow',
            'siamese',
            'wonderland',
            'foo',
            'toothpaste',
            '',
            '',
            '',
            'milky',
            'flight-manual',
            'toothpick',
            '',
            None,
            '',
            '',
        ]
        generated = []
        filter = Filter(options)
        for word in words:
            generated.append(filter.filter(word))
        self.assertEqual(generated, res)

    def test_filter_sudden_stop(self):
        words = [
            'cow',
            'foo',
            'fish',
            'flamingo',
            'enough',
            'trampoline',
            'apollo',
        ]
        res = [
            '',
            '',
            'fish',
            'flamingo',
            None,
            '',
            '',
        ]
        filtered = []
        w = Filter(options)
        for word in words:
            filtered.append(w.filter(word))
        self.assertEqual(filtered, res)

    def test_filter_run_out(self):
        words = [
            'cow',
            'foo',
            'fish',
            'flamingo',
            'trampoline',
            'apollo',
        ]
        res = [
            '',
            '',
            'fish',
            'flamingo',
            'trampoline',
            'apollo',
        ]
        w = Filter(options)
        filtered = []
        for word in words:
            filtered.append(w.filter(word))
        self.assertEqual(filtered, res)

    def test_filter_finish_same_as_stop(self):
        words = [
            'cow',
            'foo',
            'fish',
            'flamingo',
            'trampoline',
            'apollo',
            'cow',
            'pancakes',
        ]
        options = {'start': 'cow', 'stop': 'Flamingo', 'finish': 'flamingo'}
        res = [
            '',
            'foo',
            'fish',
            None,
            '',
            '',
            '',
            'pancakes',
        ]
        w = Filter(options)
        filtered = []
        for word in words:
            filtered.append(w.filter(word))
        self.assertEqual(res, filtered)

if __name__ == '__main__':
    unittest.main()

