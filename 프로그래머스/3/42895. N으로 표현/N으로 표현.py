from collections import deque

def solution(N, number):
    if N == number:
        return 1
    count = 1
    Nlist = [N,-N]
    Ns = [N*int("1"*i) for i in range(2,7)]
    countlist = deque([])
    while count < 8:
        count += 1
        newNlist = []
        for num in Nlist:
            cal(num,N,newNlist)
        if count >= 4:
            for i in range(count-3):
                for num in countlist[i+1]:
                    b = Ns[i]
                    cal(num,b,newNlist)
        # elif count == 8:
        #     for i in range(count-3):
        #         for num in countlist[i]:
        #             b = Ns[i]
        #             cal(num,b,newNlist)
        newNlist.append(N*int("1"*count))
        Nlist = list(set(newNlist))
        if number in Nlist:
            return count
        countlist.appendleft(Nlist)
    return -1

def cal(a,b,l):
    l.append(a+b)
    l.append(a-b)
    l.append(a*b)
    l.append(a//b)