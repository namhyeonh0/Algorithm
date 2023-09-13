import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = [deque([]) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(idx):
    while graph[idx]:
        node = graph[idx].popleft()
        if visited[node] == False:
            visited[node] = idx
            bfs(node)

bfs(1)

for i in range(2,n+1):
    print(visited[i])