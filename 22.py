arr="abcdabcde"
n=len(arr)
freq=set()
left=0
maxlen=0
for i in range(n):
    while arr[i] in freq:
        freq.remove(arr[left])
        left+=1
    freq.add(arr[i])
    if i-left+1>maxlen:
        maxlen=i-left+1
        a=i
        b=left
print(arr[b:a+1])
    
    