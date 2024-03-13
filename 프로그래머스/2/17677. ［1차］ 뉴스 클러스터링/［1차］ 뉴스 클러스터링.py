#합집합 만드는 함수
def ML(list1, list2):
    while len(list1) != 0:
        ss = list1[0]
        a = list1.count(ss)
        b = list2.count(ss)
        if ss in list2:
            if a-b <= 0:
                for i in range(a):
                    list1.remove(ss)
            else:
                for i in range(a-b):
                    list2.append(ss)
                for i in range(a):
                    list1.remove(ss)
        else:
            for i in range(a):
                list2.append(ss)
                list1.remove(ss)  
    return list2

#교집합 만드는 함수
def SL(list1,list2):
    minList = []
    while len(list1) != 0:
        tt = list1[0]
        if tt in list2:
            c = list1.count(tt)
            d = list2.count(tt)
            if c >= d:
                for i in range(d):
                    minList.append(tt)
                for i in range(c):
                    list1.remove(tt)
            else:
                for i in range(c):
                    minList.append(tt)
                    list1.remove(tt)
        else:
            list1.remove(list1[0])
    return minList
            

def solution(str1, str2):
    answer = 0
    
    list1, list2 = [], []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            list1.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            list2.append(str2[i:i+2].lower())
    
    list11 = list1.copy()
    list22 = list2.copy()
    
    maxList = ML(list1,list2)
    minList = SL(list11,list22)
    
    if len(maxList) == 0:
        answer = 65536
    else:
        answer = int((len(minList)/len(maxList))*65536)
    
    return answer

