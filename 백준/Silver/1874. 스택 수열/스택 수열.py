import sys

n = int(sys.stdin.readline())
stack = [0]
pushPop = []
now = 0
isBreak = False

for _ in range(n):
    num = int(sys.stdin.readline())
    if now < num:
        cal = num - now
        for _ in range(cal):
            now += 1
            stack.append(now)
            pushPop.append('+')
        stack.pop()
        pushPop.append('-')

    else:
        if stack[-1] == num:
            stack.pop()
            pushPop.append('-')
        else:
            print('NO')
            isBreak = True
            break
    
if isBreak == False:
    for pp in pushPop:
        print(pp)