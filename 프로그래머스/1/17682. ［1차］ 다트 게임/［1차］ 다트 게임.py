def solution(dartResult):
    import re
    score = re.findall(r'\d+',dartResult)

    count = 0
    for i in dartResult:
        if i == 'S':
            score[count] = int(score[count])
            count += 1
        elif i == 'D':
            score[count] = int(score[count]) ** 2
            count += 1
        elif i == 'T':
            score[count] = int(score[count]) ** 3
            count += 1
        elif i == '*':
            if count == 1:
                score[count-1] *= 2
            else:
                score[count-1] *= 2
                score[count-2] *= 2
        elif i == '#':
            score[count-1] *= -1
    result = sum(score)
    
    return result
