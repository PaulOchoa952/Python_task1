import unittest
from task3 import concatenate_nth_letters

class TestConcatenateNthLetters(unittest.TestCase):
    def test_concatenate_nth_letters(self):
        words = ["apple", "banana", "cherry", "date"]
        expected_result = "aaee"
        self.assertEqual(concatenate_nth_letters(words), expected_result)

    def test_concatenate_nth_letters_with_short_words(self):
        words = ["yoda", "best", "has"]
        expected_result = "yes"
        self.assertEqual(concatenate_nth_letters(words), expected_result)

    def test_concatenate_nth_letters_with_empty_list(self):
        words = []
        expected_result = ""
        self.assertEqual(concatenate_nth_letters(words), expected_result)

if __name__ == '__main__':
    unittest.main()