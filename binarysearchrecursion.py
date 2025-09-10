def binarysearch(arr,left,right,key):
    if(left<=right):
        
        mid=(left+right)//2
        if arr[mid]==key:
           return mid
        elif arr[mid]<key:
          return binarysearch(arr,mid+1,right,key)
        else:
            return binarysearch(arr,left,mid-1,key)
    return -1
arr=[1,2,3,4,5,6]
print(binarysearch(arr,0,len(arr)-1,5))
    