arr=[4,2,1,2,4]
key=7
k=3
n=len(arr)
res=[]

winsum=0
left=0
for i in range(n):
    winsum+=arr[i]
    while winsum >key and left<=i:
        winsum-=arr[left]
        left+=1
    if winsum==key:
        print("Subarray with sum =", key, ":", arr[left:i+1])
        
    
    
            

