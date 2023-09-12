# Description: This file is used to test the binary_search.py file
# The test cases are generated by the copilot extension.

import unittest
import binary_search

class TestAlgorithm(unittest.TestCase):

# create four test cases methods to test the binary_search method is working correctly
    # test case 1: the target is in the array.
    # test case 2: the target is not in the array.
    # test case 3: the target is the first element in the array.
    # test case 4: the target is the last element in the array.

    def test_binary_search(self):
        # test case 1: the target is in the array.
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_binary_search_2(self):
        # test case 2: the target is not in the array.
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_binary_search_3(self):
        # test case 3: the target is the first element in the array.
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5], 1), 0)

    def test_binary_search_4(self):
        # test case 4: the target is the last element in the array.
        self.assertEqual(binary_search.binary_search([1, 2, 3, 4, 5], 5), 4)

if __name__ == '__main__':
    unittest.main()


