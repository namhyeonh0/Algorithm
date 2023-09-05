def solution(sizes):
    answer = 0
    amax = 0
    bmax = 0
    for i in sizes:
        a = i[0]
        b = i[1]
        if a < b:
            a = i[1]
            b = i[0]
        if a > amax:
            amax = a
        if b > bmax:
            bmax = b
    answer = amax * bmax    
    return answer