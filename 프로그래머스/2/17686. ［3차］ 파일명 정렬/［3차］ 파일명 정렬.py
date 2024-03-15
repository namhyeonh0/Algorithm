def solution(files):
    answer = []
    
    for file in files:
        fileName = []
        head, number, tail = "", "", ""
        headLastIndex = 0
        for i in range(len(file)):
            if file[i].isdigit() == False and len(number) == 0:
                head += file[i].lower()
            elif file[i].isdigit() == False and len(number) != 0:
                tail += file[i].lower()
            elif file[i].isdigit() and len(number) < 5 and len(tail) == 0:
                number += file[i]
            elif file[i].isdigit() and len(number) >= 5:
                tail += file[i]  
        answer.append([head,int(number),tail,files.index(file)])
        answer.sort(key = lambda x: (x[0],x[1]))
        
        answerSorted = []
        for i in range(len(answer)):
            answerSorted.append(files[answer[i][3]])
                  
    return answerSorted
