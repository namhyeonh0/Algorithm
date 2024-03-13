def solution(msg):
    answer = []
    dic = {}
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(alp)):
        dic[alp[i]] = i+1
    
    while len(msg) != 0:
        for i in range(1,len(msg)+1):
            if msg[:i] in dic and i == len(msg):
                answer.append(dic[msg[:i]])
                msg = ''
                break
            if msg[:i] in dic and i != len(msg):
                continue
            else:
                answer.append(dic[msg[:i-1]])
                dic[msg[:i]] = len(dic) + 1
                msg = msg[i-1:]
                break

    return answer