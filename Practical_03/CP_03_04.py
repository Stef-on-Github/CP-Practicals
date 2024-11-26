#Binary_Search

def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1

arr = [4,6,8,5,3,9,10]
target = 10
result = binary_search(arr, target, 0, len(arr) - 1)

if result !=-1:
    print(f"Binary Search Element found at {result}")
else:
    print("Element not found in array")
