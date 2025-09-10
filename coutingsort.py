def counting(arr):
    n=len(arr)
    max_val=max(arr)
    count=[0]*(max_val+1)
    for num in arr:
        count[num]+=1
    sorted_arr=[]
    for i in range(len(count)):
        sorted_arr.extend([i]*count[i])
    return sorted_arr
arr=[1,4,3,2,5,7]
print(counting(arr))