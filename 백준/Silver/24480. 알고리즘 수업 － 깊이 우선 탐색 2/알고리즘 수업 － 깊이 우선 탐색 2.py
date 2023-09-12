import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, r = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort(reverse=True)

order = 1

def dfs(idx):
    global order
    visited[idx] = order
    for i in graph[idx]:
        if visited[i] == False:
            order += 1
            dfs(i)

dfs(r)

for i in range(1,n+1):
    print(visited[i])