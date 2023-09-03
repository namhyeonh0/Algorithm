def solution(n, m):
    answer = []
    k = 0
    if m < n:
        n, m = m ,n
    for i in range(1,n+1):
        if n % i == 0 and m % i == 0:
            k = i
    answer.append(k)
    answer.append(n*m/k)
    return answer