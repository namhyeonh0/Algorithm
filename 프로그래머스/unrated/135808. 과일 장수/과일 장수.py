def solution(k, m, score):
    score.sort()
    n = len(score) // m
    s = 0
    for i in range(n):
        l = score[len(score)-m-m*i:len(score)-m*i]
        s += min(l) * m
    return s