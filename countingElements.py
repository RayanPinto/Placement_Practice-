arr=["Python","rachan","Python","rayan"]
count={}
for i in arr:
    count[i]=count.get(i,0)+1
print(count)