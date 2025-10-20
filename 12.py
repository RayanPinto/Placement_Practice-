arr=[1,2,3,4,5,6]
k=2
left=0
n=len(arr)
winsum=0
maxsum=0
for right in range(n):
    winsum+=arr[right]
    if right-left+1>k:
        winsum-=arr[left]
        left+=1
    
    
    if(winsum>maxsum):
        maxsum=winsum
        si=left
        ri=right
        
        
res=[]
res.extend([4,5])
print(maxsum)
print(max(res))