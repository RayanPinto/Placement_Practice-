arr=[1,2,1,3,1,2,3]
n=len(arr)
freq={}
k=2
left=0
maxlen=float('-inf')
for i in range(n):
    freq[arr[i]]=freq.get(arr[i],0)+1
    while len(freq)>k:
        freq[arr[left]]-=1
        if freq[arr[left]]==0:
            del freq[arr[left]]
        left+=1
    if len(freq)<=k:
        if i-left+1 > maxlen:
            maxlen=i-left+1
            a=left
            b=i
print(arr[left:i+1])