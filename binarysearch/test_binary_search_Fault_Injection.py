# Description: This file contains the test cases for the binary_search_Fault_Injection method


import unittest
import binary_search_Fault_Injection


class TestAlgorithm(unittest.TestCase):

    def test_binary_search(self):  # binary_search method for an item  found in the array
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # create an array
        target = 5  # add a target item
        sut = binary_search_Fault_Injection.binary_search(array, target)  # software under test
        Output = sut  # actual output
        self.assertEqual(Output, 4)

    def test_binary_search_itemNotFound(self):  # binary_search method for an item not in the array
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # enter an array
        target = 11  # add a target item
        sut = binary_search_Fault_Injection.binary_search(array, target)  # software under test
        Output = sut  # actual output
        self.assertEqual(Output, -1)

    def test_binary_search_negativeItem(self):  # binary_search method for a negative item
        array = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]  # enter an array
        target = -5  # add a target item
        sut = binary_search_Fault_Injection.binary_search(array, target)  # software under test
        Output = sut  # the binary_search method is called
        self.assertEqual(Output, 4)

    def test_binary_search_emptyArray(self):  # binary search method when string is empty
        array = []  # enter an array
        target = 5  # select a target item
        sut = binary_search_Fault_Injection.binary_search(array, target)  # here is the software under test
        Output = sut  # the binary_search method is called
        self.assertEqual(Output, -1)


if __name__ == '__main__':
    unittest.main()

