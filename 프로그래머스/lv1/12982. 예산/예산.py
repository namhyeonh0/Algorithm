def solution(d, budget):
    answer = 0
    count = 0
    l = d
    for i in range(len(d)):
        if (answer + min(l)) > budget:
            break
        else:
            answer += min(l)
            count += 1
            l.remove(min(l))
        
    return count
