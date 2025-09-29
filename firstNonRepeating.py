from collections import Counter
def rayan(arr):
    arr1=Counter(arr)
    print(arr1)
    for i in arr1:
        if arr1[i]==1:
            return i
    
arr=[4,2,3,4,2]
print(rayan(arr))