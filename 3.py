arr=[1,2,3,4,5]
k=3
n=len(arr)
summ=sum(arr[:k])
print(summ)
maxsum=0
for i in range(k,n):
    summ=summ-arr[i-k]+arr[i]
    maxsum=max(summ,maxsum)
print(maxsum)