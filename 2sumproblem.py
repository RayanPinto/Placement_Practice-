def tow_sum(arr,tar):
    res={}
    r=[]
    for i,num in enumerate(arr):
        diff=tar-num
        if diff in res:
            return res[diff],i
        res[num]=i
        print(res)
print(tow_sum([2,7,11,15], 9))  # (0,1)

            