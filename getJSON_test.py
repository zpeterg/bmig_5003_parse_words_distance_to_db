import unittest
from getJSON import getJSON

words = {
    "cow": 2,
    "siamese": 1,
    "wonderland": 1,
    "foo": 1,
    "toothpaste": 1,
    "milky": 1,
    "flight-manual": 1,
    "toothpick": 1
}


def on_word(word):
    if word == 'umbrella':
        return None
    return word + 'hi'


class GetFileTest(unittest.TestCase):
    def test_getFile_basic(self):
        self.assertEqual(words, getJSON('test_output.json'))

    def test_getFile_no_file(self):
        self.assertRaises(FileNotFoundError, getJSON, 'aaa.txt')


if __name__ == '__main__':
    unittest.main()