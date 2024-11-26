#Insertion_Sort

def insertion_sort(arr):
    n = len(arr)

    if n<=1:
        return 
    
    for i in range(1,n):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j] :
            arr[j+1]==arr[j]
            j-=1
        arr[j+1]=key


arr = [45,67,89,34,56,2,4,6]
print("Unsorted list is:")
print(arr)

insertion_sort(arr)

print("Sorted list is:")
print(arr)