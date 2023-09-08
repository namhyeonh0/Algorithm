def solution(name, yearning, photo):
    answer = []
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    a = 0
    for i in photo:
        a = 0
        for j in name:
            if j in i:
                a += score[j]
        answer.append(a)

    return answer