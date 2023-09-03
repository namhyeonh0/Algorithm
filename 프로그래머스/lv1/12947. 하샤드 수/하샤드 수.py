def solution(x):
    a = str(x)
    b = 0
    for i in range(len(a)):
        b += int(a[i])
    if x % b == 0:
        answer = True
    else:
        answer = False
    return answer