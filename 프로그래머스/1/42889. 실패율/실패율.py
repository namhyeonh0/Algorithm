def solution(N, stages):
    answer = {}
    ans = []
    n = len(stages)
    for i in range(1,N+1):
        if n != 0:
            c = stages.count(i)
            rate = c/n
            n -= c
            answer[i] = rate
        else:
            answer[i] = 0
    answer = sorted(answer,key=lambda x:answer[x],reverse=True)
        
    return answer