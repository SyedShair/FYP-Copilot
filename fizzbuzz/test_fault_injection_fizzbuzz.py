# Description: This file contains manual testcases for fault_injection_fizzbuzz function
import unittest
import fault_injection_fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):  # fizzbuzz function with input value 15
        Input = 15  # input
        expectedOutput = "FizzBuzz"  # expectedOutput
        sut = fault_injection_fizzbuzz.fizz_buzz(Input)  # software under test
        output = sut  # result
        self.assertEqual(output, expectedOutput)  # compare the actual and expectedOutput

    def test_fizz(self):  # fizzbuzz function with input value 3
        Input = 3  # input
        expectedOutput = "Fizz"  # expectedOutput
        sut = fault_injection_fizzbuzz.fizz_buzz(Input)  # software under test
        output = sut  # result
        self.assertEqual(output, expectedOutput)  # compare the actual and expectedOutput

    def test_buzz(self):  # fizzbuzz function with input value 5
        Input = 5  # input
        expectedOutput = "Buzz"  # expectedOutput
        sut = fault_injection_fizzbuzz.fizz_buzz(Input)  # software under test
        output = sut  # result
        self.assertEqual(output, expectedOutput)  # compare the actual and expectedOutput

    def test_number(self):  # fizzbuzz function with input value 4
        Input = 4  # input
        expectedOutput = "4"  # expectedOutput
        sut = fault_injection_fizzbuzz.fizz_buzz(Input)  # software under test
        output = sut  # result
        self.assertEqual(output, expectedOutput)  # compare the actual and expectedOutput


if __name__ == '__main__':
    unittest.main()
