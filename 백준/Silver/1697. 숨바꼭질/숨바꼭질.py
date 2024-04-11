from collections import deque

n, k = map(int,input().split())
subin = deque()
subin.append([n])
time = 0
checked = [False for _ in range(100001)]

def bfs(subin,k):
    global time

    while subin:
        nowcheck = subin.popleft()
        nextcheck = []
        for num in nowcheck:
            if num == k:
                return time
            if num == 0:
                if checked[num+1] == False:
                    nextcheck.append(num+1)
                    checked[num+1] = True
            elif num < k:
                if checked[num+1] == False:
                    nextcheck.append(num+1)
                    checked[num+1] = True
                if checked[num-1] == False:
                    nextcheck.append(num-1)
                    checked[num-1] = True
                if num*2 <= k+1 and checked[num*2] == False:
                    nextcheck.append(num*2)
                    checked[num*2] = True
            elif num > k:
                if checked[num-1] == False:
                    nextcheck.append(num-1)
                    checked[num-1] = True
        subin.append(nextcheck)
        time += 1

print(bfs(subin,k))