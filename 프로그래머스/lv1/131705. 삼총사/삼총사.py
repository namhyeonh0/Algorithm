def solution(number):
    answer = []
    for i in range(len(number)-2):
        for j in range(i+1,len(number)-1):
            for k in range(j+1,len(number)):
                answer.append([number[i],number[j],number[k]])
    count = 0
    for i in range(len(answer)):
        if sum(answer[i]) == 0:
            count += 1
    return count