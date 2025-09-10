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
arr=[5,4,2,5,73,1,1,45,67]
key=67
for i ,j in enumerate(arr):
    if arr[i]==key:
         print(arr[i])
         
    
arr.sort()
print(binaryserch(arr,key))