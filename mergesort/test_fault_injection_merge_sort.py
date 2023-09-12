# description: manual test cases for fault injection merge_sort.py
import unittest
import fault_injection_merge_sort as main


class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):  # merge_sort function with unsorted array

        array = [1, 2, 7, 4, 9, 6, 3, 8, 5]  # unsorted array
        expectedOutput = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # sorted array
        sut = main.merge_sort(array)  # system under test
        testOutput = sut
        self.assertEqual(testOutput, expectedOutput)  # compare the expected output with the actual output

    def test_merge_sort_empty(self):  # merge_sort function with empty array

        array = []  # empty array
        expectedOutput = []  # empty array
        sut = main.merge_sort(array)  # system under test
        testOutput = sut
        self.assertEqual(testOutput, expectedOutput)  # compare the expected output with the actual output

    def test_merge_sort_duplicateItem(self):  # merge_sort function with duplicate items
        array = [1, 9, 3, 7, 5, 6, 7, 8, 2, 9]  # array with duplicate items
        expectedOutput = [1, 2, 3, 5, 6, 7, 7, 8, 9, 9]  # sorted array
        sut = main.merge_sort(array)  # system under test
        testOutput = sut
        self.assertEqual(testOutput, expectedOutput)  # compare the expected output with the actual output

    def test_merge_sort_mixedItem(self):  # merge_sort function with mixed items
        array = [3, 4, 2, 5, 1, 0, 7, 6, 8, -6, -8, -5, -3, -2, -1]  # array with mixed items
        expectedOutput = [-8, -6, -5, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]   # sorted array
        sut = main.merge_sort(array)  # system under test
        testOutput = sut
        self.assertEqual(testOutput, expectedOutput)  # compare the expected output with the actual output


if __name__ == '__main__':

    unittest.main()
