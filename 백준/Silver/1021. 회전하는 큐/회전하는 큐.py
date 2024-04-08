from collections import deque

n, m = map(int,input().split())
idx = list(map(int,input().split()))

d = deque([i for i in range(1,n+1)])
count = 0

for id in idx:
    while True:
        if id == d[0]:
            d.popleft()
            break
        else:
            if d.index(id) < len(d)/2:
                while id != d[0]:
                    d.append(d.popleft())
                    count += 1
            else:
                while id != d[0]:
                    d.appendleft(d.pop())
                    count += 1

print(count)