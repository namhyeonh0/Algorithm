def solution(n):
    answer = []
    m = str(n)
    for i in range(len(m)):
        answer.append(int(m[i]))
    answer.reverse()
    return answer