def solution(s):
    answer = {}
    result = []
    idx = 0
    for i in s:
        if i not in answer:
            answer[i] = idx
            idx += 1
            result.append(-1)
        else:
            result.append(idx-answer[i])
            answer[i] = idx
            idx += 1
    return result