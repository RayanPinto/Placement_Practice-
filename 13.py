arr=[1,3,24,5,6,7]
n=len(arr)
from collections import deque
dq=deque()
k=3
res=[]
m=mm=0
for i in range(n-k+1):
    m=arr[i:i+k]
    print(m)
    
    
    