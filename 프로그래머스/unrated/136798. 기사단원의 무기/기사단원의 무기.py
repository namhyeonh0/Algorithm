def solution(number, limit, power):
    answer = [1 for _ in range(number+1)]
    answer[0] = 0
    weight = 0
    for i in range(2,number+1):
        for j in range(i,number+1,i):
            answer[j] += 1
    count = 0
    for i in range(1,limit+1):
        a = answer.count(i)
        weight += i * a
        count += a
    weight += (number-count) * power
    return weight