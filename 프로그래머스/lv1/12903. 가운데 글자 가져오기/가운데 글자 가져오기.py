def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        n = int((len(s)/2))
        answer += s[n-1]
        answer += s[n]
    else:
        n = int((len(s)-1)/2)
        answer += s[n]
    return answer