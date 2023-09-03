def solution(n):
    m = str(n)
    answer = []
    ans = ''
    for i in range(len(m)):
        answer.append(m[i])
    answer.sort()
    answer.reverse()
    for j in range(len(answer)):
        ans += answer[j]
    return int(ans)