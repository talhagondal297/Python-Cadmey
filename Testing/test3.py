import unittest
from test1 import get_full_name

class NamesTestCase(unittest.TestCase):
    def test_first_last(self):
        full_name = get_full_name('Usman', 'Abid')
        self.assertEqual(full_name, 'Usman Abid')

unittest.main()