def solution(dartResult):
    
    score = []
    for i in range(len(dartResult)-1):
        if dartResult[i].isdigit() and dartResult[i+1].isdigit():
            score.append(dartResult[i:i+2])
        elif dartResult[i-1].isdigit() and dartResult[i].isdigit():
            continue
        elif dartResult[i].isdigit():
            score.append(dartResult[i])

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
