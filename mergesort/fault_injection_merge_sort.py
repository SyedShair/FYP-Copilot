# Description: Main file for the project of merge sort algorithm with fault injection
# here I inject a fault in the merge_sort function by changing the division operator from / to //
# in order to validate the test cases.
# Function to sort the
def merge_sort(array):
    if len(array) > 1:  # assert fault here
        mid = len(array) / 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1

            else:
                array[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array
