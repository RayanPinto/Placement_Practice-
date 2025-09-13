def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        min_value=arr.pop(min_index)
        arr.insert(i,min_value)
    return arr
arr=[1,6,5,3,2,4,5,2,3,4,1]
print(selectionsort(arr))