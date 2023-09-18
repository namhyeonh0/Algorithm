from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(q1)
    s2 = sum(q2)
    s = s1 + s2
    ave = s / 2
    count = 0
    q3 = q1 + q2
    count_limit = len(q1) * 3 - 3
    
    if s % 2 != 0:
        return -1
    elif max(q3) > ave:
        return -1
    
    while True:
        if count > count_limit:
            count = -1
            break
        elif s1 > ave:
            a = q1.popleft()
            q2.append(a)
            s1 -= a
            s2 += a
            count += 1
        elif s2 > ave:
            a = q2.popleft()
            q1.append(a)
            s1 += a
            s2 -= a
            count += 1
        elif sum(q1) == ave:
            break
            
    return count
