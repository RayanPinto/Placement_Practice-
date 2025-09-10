def quicksort(arr):
    n=len(arr)
    if len(arr)<=1:
        return arr
    pivot=arr[n//2]
    left=[x for x in arr if x<pivot]
    mid=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quicksort(left)+mid+quicksort(right)
arr=[3,3,5,75,2,11,3,45,663,3,23,43]
print(quicksort(arr))
