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
    answer = sorted(answer.items(),key=lambda x:x[1],reverse=True)
    for i in range(N):
        ans.append(answer[i][0])
        
        
    return ans