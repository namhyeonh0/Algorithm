from collections import deque

def bfs(personcheck,firecheck,room,w,h):
    global time
    escape = False
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while personcheck:
        time += 1
        personNowcheck = personcheck.popleft()
        personNextcheck = []
        fireNowcheck = firecheck.popleft()
        fireNextcheck = []
        for fireNow in fireNowcheck:
            fireNow_x = fireNow[1]
            fireNow_y = fireNow[0]
            for i in range(4):
                fireNew_x = fireNow_x + dx[i]
                fireNew_y = fireNow_y + dy[i]
                if fireNew_x >= 0 and fireNew_x < w and fireNew_y >= 0 and fireNew_y < h:
                    if room[fireNew_y][fireNew_x] == '.' or room[fireNew_y][fireNew_x] == '@':
                        fireNextcheck.append([fireNew_y,fireNew_x])
                        room[fireNew_y][fireNew_x] = '*'

        for personNow in personNowcheck:
            personNow_x = personNow[1]
            personNow_y = personNow[0]
            if personNow_x == 0 or personNow_x == w-1 or personNow_y == 0 or personNow_y == h-1:
                escape = True
                return escape
            for i in range(4):
                personNew_x = personNow_x + dx[i]
                personNew_y = personNow_y + dy[i]
                if personNew_x >= 0 and personNew_x < w and personNew_y >= 0 and personNew_y < h:
                    if room[personNew_y][personNew_x] == '.':
                        personNextcheck.append([personNew_y,personNew_x])
                        room[personNew_y][personNew_x] = '@'
        if personNextcheck:
            personcheck.append(personNextcheck)
            firecheck.append(fireNextcheck)
    
    return escape

n = int(input())
for _ in range(n):
    w, h = map(int,input().split())
    room = [list(input()) for _ in range(h)]
    time = 0
    person = []
    fire = []
    for i in range(h):
        for j in range(w):
            if room[i][j] == '@':
                person.append([i,j])
            elif room[i][j] == '*':
                fire.append([i,j])
    personcheck = deque()
    firecheck = deque()
    personcheck.append(person)
    firecheck.append(fire)
    if bfs(personcheck,firecheck,room,w,h) == True:
        print(time)
    else:
        print('IMPOSSIBLE')