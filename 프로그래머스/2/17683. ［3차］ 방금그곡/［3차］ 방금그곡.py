def solution(m, musicinfos):
    answer = []
    notesList = []
    for music in musicinfos:
        infos = music.split(",")
        hour = int(infos[1][0:2]) - int(infos[0][0:2])
        minute = int(infos[1][3:5]) - int(infos[0][3:5])
        time = hour * 60 + minute
        notes = ""
        count = 0
        while count < time:
            for i in range(len(infos[3])):
                if infos[3][i].isalpha():
                    if i != len(infos[3])-1 and infos[3][i+1].isalpha() == False:
                        notes += infos[3][i] + infos[3][i+1]
                    else:
                        notes += infos[3][i]
                    count += 1
                if count == time:
                    break
        test = m + "#"
        if notes.count(m)-notes.count(test) > 0:
            if len(answer) == 0:
                answer = [time, infos[2]]
            else:
                if time > answer[0]:
                    answer = [time, infos[2]]
    if len(answer) == 0:
        result = "(None)"
    else:
        result = answer[1]
        
        # notesList.append(notes)
#     test = m + "#"
#     for i in range(len(notesList)):
#         print(notesList[i])
#         count_real = notesList[i].count(m)
#         if count_real == 0:
#             answer = "(None)"
#         else:
#             if notesList[i].find(m) == notesList[i].find(test):
#                 answer = "(None)"
#                 continue
#             else:
#                 answer = musicinfos[i].split(",")[2]
#                 break
              
    return result