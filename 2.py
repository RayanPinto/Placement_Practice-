from collections import deque


def rayan(n)->int:
    q=deque()
    q.append([n,0])
    print(q)
    v=set()
    while q:
        x,y=q.popleft()
        if(x==0):
            return y
        if x in v:
            continue
        v.add(x)
        print(v)
        q.append((x-1,y+1))
        print(q)
        q.append((x//2,y+1))
        print(q)
        q.append((x-(2*x//2),y+1))
        print(q)
    return 0
print(rayan(5))