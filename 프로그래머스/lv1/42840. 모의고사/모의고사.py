import numpy as np

def solution(answers):
    person = {1: [1,2,3,4,5], 2: [2,1,2,3,2,4,2,5], 3: [3,3,1,1,2,2,4,4,5,5]}
    answer = []
    realAnswer = []
    for i in person:
        n = len(person[i])
        arr = np.array(person[i])
        count = 0
        if len(answers) >= n:
            m = len(answers) // len(arr)
            for j in range(m):
                l = np.array(answers[n*j:n*(j+1)])
                result = np.equal(arr,l)
                for k in result:
                    if k == True:
                        count += 1
            rest = len(answers) % n
            if rest != 0:
                restList = np.array(answers[len(answers)-rest:])
                restArr = arr[:len(restList)]
                result = np.equal(restList,restArr)
                for j in result:
                    if j == True:
                        count += 1
        if len(answers) < n:
            shortArr = arr[:len(answers)]
            answers = np.array(answers)
            result = np.equal(shortArr,answers)
            for j in result:
                if j == True:
                    count += 1
        answer.append(count)
    maxAnswer = max(answer)
        
    for i in range(len(answer)):
        if answer[i] == maxAnswer:
            realAnswer.append(i+1)
    return realAnswer

