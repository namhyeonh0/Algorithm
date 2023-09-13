import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(idx1,idx2):
    
    visited, need_visit = [], [[]]
    need_visit[0].append(idx1)
    chonsu = 0

    while need_visit:

        if idx2 in need_visit[0]:
            break

        else:
            now_visit = need_visit.pop()
            next_visit = []

            for i in now_visit:
                if i in visited:
                    continue
                else:
                    visited.append(i)
                    for j in graph[i]:
                        if j not in visited:
                            next_visit.append(j)

            if len(next_visit) == 0:
                chonsu = -1
                break

            need_visit.append(next_visit)

        chonsu += 1
        
    print(chonsu)

bfs(a,b)