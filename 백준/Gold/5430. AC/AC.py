from collections import deque

t = int(input())

for _ in range(t):
    func = input()
    n = int(input())
    nums = input()
    nums = nums[1:len(nums)-1]
    if n != 0:
        nums = deque(nums.split(','))
    else:
        nums = []
    rev = False
    err = False
    
    for f in func:
        if f == 'R':
            rev = True if rev == False else False
        elif f == 'D':
            if nums:
                if rev == True:
                    nums.pop()
                else:
                    nums.popleft()
            else:
                print('error')
                err = True
                break
    nums = list(nums)
    
    if rev == True and err == False:
        print('[' + ','.join(nums[::-1]) + ']')
    elif rev == False and err == False:
        print('[' + ','.join(nums) + ']')