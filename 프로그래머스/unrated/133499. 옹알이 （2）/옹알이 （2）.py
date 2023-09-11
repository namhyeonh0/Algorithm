def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling:
        word = ''
        l = []
        for j in i:
            word += j
            if word in baby:
                l.append(word)
                word = ''
                if len(l) >= 2 and l[-1] == l[-2]:
                    break
        else:
            if len(word) == 0:
                answer += 1
    return answer

