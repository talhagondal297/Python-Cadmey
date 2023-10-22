import unittest
from test4 import get_full_name


class NamesTestCase(unittest.TestCase):

    def test_first_last(self):
        full_name = get_full_name('Ahmed', 'Ahad')
        self.assertEqual(full_name, 'Ahmad Ahad ')

    def test_middle(self):
        full_name = get_full_name('Muhammad', 'Arslan', 'Altaf')
        self.assertEqual(full_name, 'Muhammad Arslan Altaf ')


unittest.main()