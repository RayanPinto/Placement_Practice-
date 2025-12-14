arr=[5,2,-1,0,3,2]
n=len(arr)
k=3
window=set()
maxsum=float('-inf')
winsum=0
left=0
start_index=end_index=0
for right in range(n):
    while arr[right] in window:
        window.remove(arr[left])
        winsum-=arr[left]
        left+=1
    window.add(arr[right])
    winsum+=arr[right]
    if right-left+1>k:
        window.remove(arr[left])
        left+=1
        winsum-=arr[left]
        left+=1
    if(winsum>maxsum):
        maxsum=winsum
        start_index=left
        end_index=right
        
print(maxsum)
print(start_index,end_index)
print(f"subarray :{arr[start_index:end_index+1]}")
    