def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
            
    return arr
arr=[3,3,5,75,2,11,3,45,663,3,23,43]
print(selectionsort(arr))
                