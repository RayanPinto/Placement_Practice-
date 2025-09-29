arr=[1,2,3,4,5,4,2]
seen=set()
res=[]
for i in arr:
    if i not in seen:
        seen.add(i)
    else:
        res.append(i)
print(res)
        