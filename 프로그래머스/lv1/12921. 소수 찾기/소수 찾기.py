def solution(n):
    l = [0 for _ in range(n+1)]
    l[0] = 1
    l[1] = 1
    for i in range(2,n+1):
        if l[i] == 1:
            continue
        for j in range(i*2,n+1,i):
            l[j] = 1
    c = l.count(0)
    return c
