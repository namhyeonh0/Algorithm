def solution(n, m, section):
    answer = 0
    l = [0 for _ in range(n+1)]
    l[0] = 1
    count = 0
    for i in section:
        if l[i] == 0:
            if len(l) >= i+m:
                for j in range(i,i+m):
                    l[j] = 1
                count += 1
            else:
                for j in range(i,len(l)):
                    l[j] = 1
                count += 1
    return count