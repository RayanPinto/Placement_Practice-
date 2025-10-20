from collections import deque

def max_sliding_window(arr, k):
    dq = deque()   # will store indexes
    result = []

    for i in range(len(arr)):
        print(i)
        if dq and dq[0]==i-k:
            print(dq)
            dq.popleft()
            print(dq)
        while dq and arr[dq[-1]]<arr[i]:
            print(dq)
            dq.pop()
            print(dq)
        dq.append(i)
        print(dq)
    if i>=k-1:
        result.append(arr[dq[0]])
            

# Example:
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_sliding_window(arr, k))  # [3, 3, 5, 5, 6, 7]
