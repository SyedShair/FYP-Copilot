# Description:binary search algorithm with a fault
# fault: the mid is calculated by (left + right) / 2 instead of (left + right) // 2
def binary_search(array, target):
    if len(array) == 0:
        return -1
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) / 2  # fault is here
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1











