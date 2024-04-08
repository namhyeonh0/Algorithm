from collections import deque

t = int(input())

for _ in range(t):
    func = input()
    n = int(input())
    nums = input()
    nn = nums[1:len(nums)-1]
    if n != 0:
        nnn = deque(nn.split(','))
    else:
        nnn = []
    rev = False
    err = False
    
    for f in func:
        if f == 'R':
            rev = True if rev == False else False
        elif f == 'D':
            if nnn:
                if rev == True:
                    nnn.pop()
                else:
                    nnn.popleft()
            else:
                print('error')
                err = True
                break
    nnn = list(nnn)
    
    if rev == True and err == False:
        print('[' + ','.join(nnn[::-1]) + ']')
    elif rev == False and err == False:
        print('[' + ','.join(nnn) + ']')