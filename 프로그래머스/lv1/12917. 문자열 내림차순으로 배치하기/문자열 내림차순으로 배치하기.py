def solution(s):
    answer = ''
    low = []
    upp = []
    for i in s:
        if i.isupper() == False:
            low.append(i)
        else:
            upp.append(i)
    low.sort()
    low.reverse()
    upp.sort()
    upp.reverse()
    for i in low:
        answer += i
    for i in upp:
        answer += i
    return answer