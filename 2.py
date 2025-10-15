from collections import deque
queue=deque([(5,0)])
visited=set()
while queue:
    x,y=queue.popleft()
    if x==0:
        print("we did it")
        break
    if y in visited:
        continue
    visited.add(y)
    print(visited)
    queue.append((x-1,y+1))
    print(queue)
    queue.append((x//2,y+1))
    print(queue)
    queue.append((x-(2*x/2),y+1))
    print(queue)
    

