def solution(X, Y):
    x = list(X); y = list(Y)
    x.sort(reverse=True); y.sort(reverse=True)
    setX = list(set(x)); setY = list(set(y))
    setX.sort(reverse=True); setY.sort(reverse=True)
    l = {}
    for i in setX:
        if i in setY:
            countX = x.count(i)
            countY = y.count(i)
            if countX > countY:
                l[i] = countY
            else:
                l[i] = countX
    answer = ''
    if len(l) == 0:
        answer = '-1'
    elif len(l) == 1 and '0' in l:
        answer = '0'
    else:
        for i in l:
            count = l[i]
            for _ in range(count):
                answer += str(i)
                
    return answer