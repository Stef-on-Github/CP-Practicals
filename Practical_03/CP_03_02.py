#Bubble_Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break  # Use 'break' to exit the loop if no elements were swapped


arr = [34,67,89,43,2,11,99,78]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)
