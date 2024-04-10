from collections import deque

n, m = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(n)]

row = [1, -1, 0, 0]
column = [0, 0, 1, -1]

def bfs(matrix, a, b):
    check = deque()
    check.append((a,b))
    matrix[a][b] = 0
    count = 1
    
    while check:
        x, y = check.popleft()
        for i in range(4):
            aa = x + row[i]
            bb = y + column[i]
            if 0 <= aa and aa < n and 0 <= bb and bb < m:
                if matrix[aa][bb] == 1:
                    check.append((aa,bb))
                    matrix[aa][bb] = 0
                    count += 1
    
    return count

drawings = []

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            drawings.append(bfs(paper,i,j))

if drawings:
    print(len(drawings))
    print(max(drawings))
else:
    print(0)
    print(0)