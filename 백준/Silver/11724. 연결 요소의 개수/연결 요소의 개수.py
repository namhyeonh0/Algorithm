import sys
input = sys.stdin.readline

nm = list(map(int,input().split()))
n = nm[0]
m = nm[1]

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    xy = list(map(int,input().split()))
    x = xy[0]
    y = xy[1]
    graph[x][y] = True
    graph[y][x] = True

def dfs(idx):
    
    visited[idx] = True

    for i in range(1,n+1):
        if visited[i] == False and graph[idx][i] == True:
            dfs(i)

answer = 0

for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        answer += 1
    else:
        continue

print(answer)