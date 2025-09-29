def rayan(s):
    first=max(s)
    second=0
    for i in s:
        if i>second and i<first:
            second=i
    print(first)
    print(second)
rayan([1,5,6,4])
    