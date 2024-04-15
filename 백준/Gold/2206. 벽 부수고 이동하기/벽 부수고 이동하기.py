from collections import deque

n, m = map(int,input().split())
road = [list(input()) for _ in range(n)]

def bfs(road,n,m):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    normalCheck = [[False for _ in range(m)] for _ in range(n)]
    wallBreakCheck = [[False for _ in range(m)] for _ in range(n)]
    normalCheck[0][0] = 1
    wallBreakCheck[0][0] = 1

    normalQueue = deque([[[0,0]]])
    wallBreakQueue = deque()

    while normalQueue or wallBreakQueue:
        
        if normalQueue:
            nowNowmalQueue = normalQueue.popleft()
        else: nowNowmalQueue = []
        if wallBreakQueue:
            nowWallBreakQueue = wallBreakQueue.popleft()
        else: nowWallBreakQueue = []

        nextNormalQueue = []
        nextWallBreakQueue = []

        for nowNormal in nowNowmalQueue:
            nowNormal_x = nowNormal[1]
            nowNormal_y = nowNormal[0]
            for i in range(4):
                newNormal_x = nowNormal_x + dx[i]
                newNormal_y = nowNormal_y + dy[i]
                if 0 <= newNormal_x and newNormal_x < m and 0 <= newNormal_y and newNormal_y < n:
                    if normalCheck[newNormal_y][newNormal_x] == False and road[newNormal_y][newNormal_x] == '0':
                        normalCheck[newNormal_y][newNormal_x] = normalCheck[nowNormal_y][nowNormal_x] + 1
                        nextNormalQueue.append([newNormal_y,newNormal_x])
                    elif wallBreakCheck[newNormal_y][newNormal_x] == False and road[newNormal_y][newNormal_x] == '1':
                        wallBreakCheck[newNormal_y][newNormal_x] = normalCheck[nowNormal_y][nowNormal_x] + 1
                        nextWallBreakQueue.append([newNormal_y,newNormal_x])
        
        for nowWallBreak in nowWallBreakQueue:
            nowWallBreak_x = nowWallBreak[1]
            nowWallBreak_y = nowWallBreak[0]
            for i in range(4):
                newWallBreak_x = nowWallBreak_x + dx[i]
                newWallBreak_y = nowWallBreak_y + dy[i]
                if 0 <= newWallBreak_x and newWallBreak_x < m and 0 <= newWallBreak_y and newWallBreak_y < n:
                    if wallBreakCheck[newWallBreak_y][newWallBreak_x] == False and road[newWallBreak_y][newWallBreak_x] == '0':
                        wallBreakCheck[newWallBreak_y][newWallBreak_x] = wallBreakCheck[nowWallBreak_y][nowWallBreak_x] + 1
                        nextWallBreakQueue.append([newWallBreak_y,newWallBreak_x])
        
        if nextNormalQueue:
            normalQueue.append(nextNormalQueue)
        if nextWallBreakQueue:
            wallBreakQueue.append(nextWallBreakQueue)

    normalResult = normalCheck[n-1][m-1]
    wallBreakResult = wallBreakCheck[n-1][m-1]
    if normalResult and wallBreakResult:
        print(min(normalResult,wallBreakResult))
    elif normalResult and not wallBreakResult:
        print(normalResult)
    elif not normalResult and wallBreakResult:
        print(wallBreakResult)
    else: print(-1)

bfs(road,n,m)