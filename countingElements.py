arr=["r","w","s","s","w","w"]
count={}

for i in arr:
    count[i]=count.get(i,0)+1
print(count)