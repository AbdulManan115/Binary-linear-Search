# Binary Search Implementation
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Linear Search Implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example Usage
arr = [2, 4, 6, 8, 10, 12]
target = 10

print("Binary Search Result:", binary_search(arr, target))
print("Linear Search Result:", linear_search(arr, target))
