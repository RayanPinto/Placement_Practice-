arr=[1,2,3,4,3,4,4,6,7]
n=len(arr)
winsum=0
winset=set()
maxsum=0
left=0
k=3
for right in range(n):
    while arr[right] in winset:
        
        winsum-=arr[left]
        
        winset.remove(arr[left])
        left+=1
    winsum+=arr[right]
    winset.add(arr[right])
    
    if(winsum>maxsum):
        maxsum=winsum
        start_index=left
        end_index=right
print(f"max sumbaary is :{arr[start_index:end_index+1]} and sum is {maxsum}")