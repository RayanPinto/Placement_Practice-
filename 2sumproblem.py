def twosum(arr,target):
    res={}
    for i,num in enumerate(arr):
        diff=target-num
        if diff in res:
            return res[diff],i
        res[num]=i
print(twosum(arr=[1,4,5,6,7,2,7],target=9))