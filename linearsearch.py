def rayan(arr,key):
    for i,val in enumerate(arr):
        if val==key:
            return i
arr=[3,4,53,2,23,3,5]
key=3
print(rayan(arr,key))