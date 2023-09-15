import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def worms():
    global cnt
    if len(arr) == 0:
        print(cnt)
        return 
    else:
        need_visit = deque([arr.popleft()])
    while need_visit:
        node = need_visit.popleft()
        need_remove = []
        for i in arr:
            if node[0] == i[0] and abs(node[1]-i[1]) == 1:
                need_visit.append(i)
                need_remove.append(i)
            elif node[1] == i[1] and abs(node[0]-i[0]) == 1:
                need_visit.append(i)
                need_remove.append(i)
        for i in need_remove:
            arr.remove(i)
        if len(need_visit) == 0:
            cnt += 1
            worms()
        
for _ in range(t):
    m, n, k = map(int,input().split())
    arr = deque([])
    cnt = 0
    for _ in range(k):
        x, y = map(int,input().split())
        arr.append([x,y])
    worms()