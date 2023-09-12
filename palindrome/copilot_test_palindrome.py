# generate four unittest methods to check that given string is a palindrome or not
# 1. test_palindrome
# 2. test_palindrome_with_mixed_case
# 3. test_palindrome_with_punctuation
# 4. test_palindrome_with_mixed_case_and_punctuation

import unittest
import palindrome


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(palindrome.palindrome("madam"))

    def test_palindrome_with_mixed_case(self):
        self.assertTrue(palindrome.palindrome("Madam"))

    def test_palindrome_with_punctuation(self):
        self.assertTrue(palindrome.palindrome("madam!"))

    def test_palindrome_with_mixed_case_and_punctuation(self):
        self.assertTrue(palindrome.palindrome("Madam!"))


if __name__ == '__main__':
    unittest.main()
