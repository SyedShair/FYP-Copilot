# generate four test case methods for fizzbuzz programme.
# 1. test_fizz_buzz
# 2. test_fizz
# 3. test_buzz
# 4. test_number

import unittest
import fizzbuzz


class MyTestCase(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(fizzbuzz.fizz_buzz(15), 'FizzBuzz')

    def test_fizz(self):
        self.assertEqual(fizzbuzz.fizz_buzz(3), 'Fizz')

    def test_buzz(self):
        self.assertEqual(fizzbuzz.fizz_buzz(5), 'Buzz')

    def test_number(self):
        self.assertEqual(fizzbuzz.fizz_buzz(7), '7')


if __name__ == '__main__':
    unittest.main()
