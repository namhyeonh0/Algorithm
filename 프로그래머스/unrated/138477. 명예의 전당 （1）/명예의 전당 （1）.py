def solution(k, score):
    answer = []
    l = []
    days = len(score)
    for i in range(days):
        l.append(score[i])
        if len(l) >= k+1:
            l.remove(min(l))
            answer.append(min(l))
        else:
            answer.append(min(l))
            
    return answer