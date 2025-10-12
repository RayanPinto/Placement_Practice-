def counting(arr):
    n=len(arr)
    res=[]
    max_val=max(arr)
    count=[0]*(max_val+1)
    for i in arr:
        count[i]+=1
    for i in range(len(count)):
        res.extend([i]*count[i])
    return res
arr=[1,6,5,3,2,4,5,2,3,4,1]
print(counting(arr))