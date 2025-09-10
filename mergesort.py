def mergesort(arr):
    n=len(arr)
    if n<=1:
        return arr
    mid=n//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    i=j=0
    res=[]
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
        
arr=[3,3,5,75,2,11,3,45,663,3,23,43]
print(mergesort(arr))