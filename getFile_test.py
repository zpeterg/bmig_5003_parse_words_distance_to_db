import unittest
from time import time
from getFile import getFile

words = [
    'Fish',
    'hat',
    'foo',
    'cow',
    'Cow',
    'siamese.',
    'Wonderland',
    'foo',
    'toothpaste',
    'bar',
    'umbrella',
    'foo\n',
    'milky',
    '\'"flight-manual"\'',
    'toothpick',
    'bar',
    'enough',
    'event-horizon',
    'bar!'
]


def on_word(word):
    if word == 'umbrella':
        return None
    return word + 'hi'


class GetFileTest(unittest.TestCase):
    def test_getFile_basic(self):
        self.assertEqual(words, getFile('small_test.txt', lambda a: a))

    def test_getFile_no_file(self):
        self.assertRaises(FileNotFoundError, getFile, 'aaa.txt', lambda a: a)

    def test_getFile_(self):
        res = ['Fishhi', 'hathi', 'foohi', 'cowhi', 'Cowhi', 'siamese.hi', 'Wonderlandhi', 'foohi', 'toothpastehi', 'barhi']
        self.assertEqual(res, getFile('small_test.txt', on_word))

    def test_getFile_moby(self):
        t0 = time()
        self.assertLess(100000, len(getFile('moby_test.txt', on_word)))
        t1 = time()
        print('Moby import time sec:', t1 - t0)


if __name__ == '__main__':
    unittest.main()