from collections import deque

m, n, h = map(int,input().split())
boxes = []
tomato = 0
notomato = 0
time = 0
check = deque()
for _ in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int,input().split())))
    boxes.append(box)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                tomato += 1
                check.append([i,j,k])
            elif boxes[i][j][k] == -1:
                notomato += 1

def bfs(check,boxes):
    global time
    count = 0
    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]

    while check:
        nowcheck = check.popleft()
        now_h = nowcheck[0]
        now_n = nowcheck[1]
        now_m = nowcheck[2]
        for i in range(6):
            new_h = now_h + dx[i]
            new_n = now_n + dy[i]
            new_m = now_m + dz[i]
            if 0 <= new_h and new_h < h and 0 <= new_n and new_n < n and 0 <= new_m and new_m < m:
                if boxes[new_h][new_n][new_m] == 0:
                    boxes[new_h][new_n][new_m] = boxes[now_h][now_n][now_m] + 1
                    check.append([new_h,new_n,new_m])
                    count += 1
                    time = boxes[new_h][new_n][new_m] - 1
    return count

checkedtomato = tomato + bfs(check,boxes)
checkingtomato = h*m*n - notomato
if checkedtomato == checkingtomato:
    print(time)
else:
    print(-1)