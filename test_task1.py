import unittest
from unittest.mock import patch
from task1 import Dictionary
class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary()
    def test_new_entry(self):
        self.dictionary.entries = {}
        self.dictionary.entries['test'] = 'description'
        self.assertEqual(self.dictionary.entries['test'], 'description')
    @patch('builtins.print')
    def test_print_dict(self, mock_print):
        self.dictionary.entries = {'test': 'description'}
        self.dictionary.print_dict()
        mock_print.assert_called_with('test: description')
    def test_look(self):
        self.dictionary.entries = {'test': 'description'}
        self.assertEqual(self.dictionary.look('test'), 'description')
        self.assertEqual(self.dictionary.look('nonexistent'), 'Entry not found.')
if __name__ == '__main__':
    unittest.main()