def sorting(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


ls = []
n = int(input("Enter the number of elements you want:- "))
for i in range(0,n):
    m = int(input(f"Enter the {i+1} element :- "))
    ls.append(m)

sorting(ls)
print("Sorted array is", ls)
