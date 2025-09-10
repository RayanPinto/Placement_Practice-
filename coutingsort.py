def counting(arr):
    n=len(arr)
    max_val=max(arr)
    count=[0]*(max_val+1)
    for num in arr:
        count[num]+=1
    sorted_arr=[]
    print(count)
    for i in range(len(count)):
        sorted_arr.extend([i]*count[i])
        print(sorted_arr)
    return sorted_arr
arr=[1,3,4,2,1,1,34,4,32,2,2]
print(counting(arr))