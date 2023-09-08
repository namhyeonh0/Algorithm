def solution(a, b, n):
    answer = 0
    while n >= a:
        k = n // a
        if k != 0 :
            answer += b * k
            n = n - a * k + b * k
    return answer