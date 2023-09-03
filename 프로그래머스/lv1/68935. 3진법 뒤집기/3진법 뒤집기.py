def solution(n):
    count = 0
    while True:
        if n // (3 ** count) != 0:
            count += 1
            continue
        else:
            break
    count -= 1
    l = []
    for i in range(count,-1,-1):
        if n != 0:
            l.append(n // (3 ** i))
            n -= (n // (3 ** i)) * (3 ** i)
        else:
            l.append(0)
    l.reverse()
    answer = 0
    newCount = len(l) - 1
    for i in range(len(l)):
        answer += l[i] * (3 ** newCount)
        newCount -= 1
    return answer