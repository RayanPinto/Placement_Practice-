def r(arr,k):
    n=len(arr)
    k=k%n
    print(k)
    return arr[-k:]+arr[:-k]
arr=[1,2,3,4,5]
print(r(arr,7))