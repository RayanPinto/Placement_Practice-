def twosum(arr,target):
    res={}
    for i,j in enumerate(arr):
        diff=target-j
        if diff in res:
            return (res[diff],i)
        res[j]=i
    return (-1,-1)
print(twosum(arr=[1,4,5,6,7,2,7],target=9))