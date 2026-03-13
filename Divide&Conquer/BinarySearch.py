"""
Problem: Need to implement a binary search algorithm to find the index
of a target value in a array.
Result is in the README
"""
def binary_search(arr, target):
    left = 0 # left most index
    right = len(arr) - 1 # right most index

    # As long as the left index is less than or equal to the right index, we will continue
    # to divide the array in half and check if the middle element is the target. If it is, we return the index.
    # If the middle element is less than the target, we know that the target must be in the right half of the array, so we move the left index to mid + 1. 
    # If the middle element is greater than the target, we know that the target must be in the left half of the array, so we move the right index to mid - 1.
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 

numbers = [1, 3, 5, 7, 9, 11]

result = binary_search(numbers, 7)
print(f" BINARY SEARCH: {numbers} contains 7 at index: {result}")