"""
Problem: Need to Implement the merge sort algorithm to sort an array of integers.
Result is in the README
"""

def merge_sort(arr): # This function takes an array as input and returns a sorted array 
    if len(arr) <= 1: 
        return arr 
    mid = len(arr) // 2
    left = merge_sort(arr[:mid]) # Recursively sort the left half of the array
    right = merge_sort(arr[mid:]) # Recursively sort the right half of the array

    return merge(left, right)
# The merge function takes two sorted arrays as input and returns a single sorted array
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]) 
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:]) 
    result.extend(right[j:])

    return result

numbers = [8, 3, 5, 2, 9, 1]

sorted_numbers = merge_sort(numbers)
print("MERGE SORT:")
print(f"Original array: {numbers}")
print(f"Sorted array: {sorted_numbers}")