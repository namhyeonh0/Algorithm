from collections import deque

n = int(input())
count = 1
answer = 0
l = deque([0,1])

def pivo(i):
    global count, answer, l
    count += 1
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        if count <= i:
            answer = sum(l)
            l.popleft()
            l.append(answer)
            return pivo(i)
        else:
            return l.pop()

print(pivo(n))