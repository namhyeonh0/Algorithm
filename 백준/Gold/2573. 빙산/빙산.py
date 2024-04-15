from collections import deque

n, m = map(int,input().split())
sea = [list(map(int,input().split())) for _ in range(n)]
water = [[True for _ in range(m)] for _ in range(n)]
count_ice = 0
ice = []
for i in range(n):
    for j in range(m):
        if sea[i][j] != 0:
            count_ice += 1
            ice.append([i,j])
            water[i][j] = False

def bfs2(sea,count_ice,iceCheck,n,m):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    check = [[False for _ in range(m)] for _ in range(n)]
    check[iceCheck[0]][iceCheck[1]] = True
    count = 1
    queue = deque([[iceCheck[0],iceCheck[1]]])

    while queue:
        now = queue.popleft()
        now_x = now[1]
        now_y = now[0]
        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]
            if 0 <= new_x and new_x < m and 0 <= new_y and new_y < n:
                if check[new_y][new_x] == False and sea[new_y][new_x] != 0:
                    check[new_y][new_x] = True
                    count += 1
                    queue.append([new_y,new_x])
    
    if count == count_ice:
        return True
    else: return False

def bfs1(sea,water,count_ice,ice,n,m):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque([ice])
    year = 0

    while queue:

        nowQueue = queue.popleft()
        nextQueue = []
        toWater = []
        iceCheck = nowQueue[0]
        if bfs2(sea,count_ice,iceCheck,n,m) == False:
            return year

        for now in nowQueue:
            now_x = now[1]
            now_y = now[0]
            for i in range(4):
                new_x = now_x + dx[i]
                new_y = now_y + dy[i]
                if 0 <= new_x and new_x < m and 0 <= new_y and new_y < n:
                    if water[new_y][new_x] == True:
                        sea[now_y][now_x] -= 1
            if sea[now_y][now_x] <= 0:
                sea[now_y][now_x] = 0
                count_ice -= 1
                toWater.append([now_y,now_x])
            else:
                nextQueue.append([now_y,now_x])
        
        for towater in toWater:
            water[towater[0]][towater[1]] = True
        
        if nextQueue:
            queue.append(nextQueue)
        
        year += 1
    
    return 0

print(bfs1(sea,water,count_ice,ice,n,m))