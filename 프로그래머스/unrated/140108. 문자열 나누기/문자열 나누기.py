def solution(s):
    answer = 0
    while len(s):
        x = s[0]
        x_count = 0
        notx_count = 0
        for i in range(len(s)):
            if s[i] == x:
                x_count += 1
                
            else:
                notx_count += 1
                
            if x_count == notx_count:
                s = s[i+1:]
                answer += 1
                break
        else:
            answer += 1
            break
        
    return answer