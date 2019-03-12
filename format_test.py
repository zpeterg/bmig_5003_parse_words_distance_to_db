import unittest
from format import formatToLines

arr = [('foo', 2), ('bar', 2), ('fish', 0), ('stapler', 3)]

class FormatTest(unittest.TestCase):
    def test_format_to_columns(self):
        res = [
            'foo              2                ',
            'bar              2                ',
            'fish             0                ',
            'stapler          3                ',
        ]
        self.assertEqual(formatToLines(arr, 2), res)

if __name__ == '__main__':
    unittest.main()

