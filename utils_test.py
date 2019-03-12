import unittest
from utils import dealArgs, cleanWord


args = [
    '--input=small_test.txt',
    '--start=foo',
    '--stop=bar',
    '--finish=enough',
    '-c',
]


class UtilsTest(unittest.TestCase):
    def test_deal_args(self):
        res = {
            'files': ['small_test.txt'],
            'start': 'foo',
            'stop': 'bar',
            'finish': 'enough',
            'clear': True,
        }
        options = dealArgs(args)
        self.assertEqual(res, options.to_object())

    def test_multi_file(self):
        res = {
            'file': ['small_test.txt', 'small_test2.txt'],
            'start': 'foo',
            'stop': 'bar',
            'finish': 'enough',
            'clear': True,
        }

    def test_change_file(self):
        options = dealArgs(args)
        options.files = ['foo.txt']
        self.assertEqual(['foo.txt'], options.files)

    def test_change_clear(self):
        options = dealArgs(args)
        options.clear = True
        self.assertEqual(True, options.clear)

    def test_deal_no_args(self):
        self.assertRaises(ValueError, dealArgs, [])

    def test_clean_word(self):
        arr = ['@##it(#)', '\'"is#', '(($(`+)=-t1me{};<>?,./', 'for', 'A11', ' g00d ', '4', '!@#$%^&*()', ' ']
        res = ['it', 'is', 't1me', 'for', 'a11', 'g00d', '4', '', '']
        cleaned = []
        for word in arr:
            cleaned.append(cleanWord(word))
        self.assertEqual(res, cleaned)

if __name__ == '__main__':
    unittest.main()

