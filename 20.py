arr=[4,5,4,5,2]
n=len(arr)
max_len=0
k=2
left=0
freq={}
for i in range(n):
    freq[arr[i]]=freq.get(arr[i],0)+1
    while len(freq)>k:
        freq[arr[left]]-=1
        
        if freq[arr[left]]==0:
            del freq[arr[left]]
        left+=1
    if len(freq)==k:
        if i-left+1>max_len:
            max_len=i-left+1
            a=left
            b=i
print(arr[a:b+1])