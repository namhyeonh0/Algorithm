def solution(t, p):
    answer = 0
    n = len(t)
    m = len(p)
    for i in range(n-(m-1)):
        three = ''
        for j in range(i,m+i):
            three += t[j]
        if int(three) <= int(p):
            answer += 1
    return answer