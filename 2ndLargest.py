def rayan(arr):
    num1=max(arr)
    num2=0
    for i in arr:
        if num1>i>num2:
            num2=i
    return num1,num2
print(rayan(arr=[2,3,4,5]))