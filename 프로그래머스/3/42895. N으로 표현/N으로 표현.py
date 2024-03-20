from collections import deque

def solution(N, number):
    if N == number:
        return 1
    answer = 0
    count = 1
    Nlist = [N,-N]
    Ns = [N*11,N*111,N*1111,N*11111,N*111111]
    countlist = deque([])
    while count <= 8:
        count += 1
        newNlist = []
        for num in Nlist:
            for i in range(4):
                if i == 0:
                    newNlist.append(num+N)
                elif i == 1:
                    newNlist.append(num-N)
                elif i == 2:
                    newNlist.append(num*N)
                else:
                    newNlist.append(num//N)
        if count >= 4 and count <= 7:
            for i in range(count-3):
                for num in countlist[i+1]:
                    newNlist.append(num+Ns[i])
                    newNlist.append(num-Ns[i])
                    newNlist.append(num*Ns[i])
                    newNlist.append(num//Ns[i])
        elif count == 8:
            for i in range(count-3):
                for num in countlist[i]:
                    newNlist.append(num+Ns[i])
                    newNlist.append(num-Ns[i])
                    newNlist.append(num*Ns[i])
                    newNlist.append(num//Ns[i])

        newNlist.append(N*int("1"*count))
        Nlist = list(set(newNlist))
        if count >=2 and count <= 6:
            countlist.appendleft(Nlist)
        if number in Nlist:
            return count
    return -1


