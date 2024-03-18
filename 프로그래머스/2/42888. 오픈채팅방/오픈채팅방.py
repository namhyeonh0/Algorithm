def solution(record):
    answer = []
    userID_index = {}
    userID_name = {}
    idx = 0
    
    for string in record:
        stringList = string.split(" ")
        if stringList[0] == "Enter":
            if stringList[1] not in userID_index:
                answer.append(stringList[2] + "님이 들어왔습니다.")
                userID_index[stringList[1]] = [idx]
                userID_name[stringList[1]] = stringList[2]
            else:
                for i in userID_index[stringList[1]]:
                    preName1 = answer[i][:answer[i].find("님")]
                    answer[i] = answer[i].replace(preName1,stringList[2])
                answer.append(stringList[2] + "님이 들어왔습니다.")
                userID_index[stringList[1]].append(idx)
                userID_name[stringList[1]] = stringList[2]
            idx += 1
        elif stringList[0] == "Leave":
            answer.append(userID_name[stringList[1]] + "님이 나갔습니다.")
            userID_index[stringList[1]].append(idx)
            idx += 1
        else:
            for i in userID_index[stringList[1]]:
                preName2 = answer[i][:answer[i].find("님")]
                answer[i] = answer[i].replace(preName2,stringList[2])
            userID_name[stringList[1]] = stringList[2]
                
    return answer
