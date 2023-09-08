def solution(food):
    answer = ''
    for i in range(1,len(food)):
        for j in range(food[i]//2):
            answer += '{}'.format(i)
    answer_reverse = answer[::-1]
    answer = answer + '0' + answer_reverse
    return answer