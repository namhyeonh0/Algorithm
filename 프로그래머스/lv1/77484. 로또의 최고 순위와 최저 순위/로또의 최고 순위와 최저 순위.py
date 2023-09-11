def solution(lottos, win_nums):
    answer = [0,0]
    count0 = lottos.count(0)
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    l = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    high = count0+count
    low = count
    answer[0] = l[high]
    answer[1] = l[low]
    return answer