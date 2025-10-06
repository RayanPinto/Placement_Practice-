def binaryserch(arr,key):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[1,2,3,4,5,6,7,1,2,3,5,6,7]
key=7

         

arr.sort()
print(arr)
print(binaryserch(arr,key))