import sys
input = sys.stdin.readline

n, m, v = map(int,input().split())

graph = [[] for _ in range(n+1)]
dfs_visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

dfs_order = ''
bfs_order = ''

def dfs(idx):

    global dfs_order
    dfs_visited[idx] = True
    dfs_order += str(idx) + ' '

    for i in graph[idx]:
        if dfs_visited[i] == False:
            dfs(i)

def bfs(idx):

    from collections import deque
    global bfs_order

    bfs_visited = []; bfs_need_visit = deque([]);
    bfs_need_visit.append(idx)

    while bfs_need_visit:
        node = bfs_need_visit.popleft()
        if node in bfs_visited:
            continue
        else:
            bfs_visited.append(node)
            bfs_need_visit.extend(graph[node])
            bfs_order += str(node) + ' '
            
dfs(v)
bfs(v)

print(dfs_order + '\n' + bfs_order)