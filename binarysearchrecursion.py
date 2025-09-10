def binarysearch(arr,key,left,right):
    if(left<=right):
        mid=(left+right)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            return binarysearch(arr,key,mid+1,right)
        else:
            return binarysearch(arr,key,left,mid-1)
    return -1
arr=[1,2,3,4,5,6]
key=6
print(binarysearch(arr,key,0,len(arr)-1))