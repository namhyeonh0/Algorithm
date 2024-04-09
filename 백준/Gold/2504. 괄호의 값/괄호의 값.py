string = input()
stack = []
total = 0
now = 1
isBreak = False

for i in range(len(string)):
    if string[i] == '(':
        stack.append(string[i])
        now *= 2
    elif string[i] == '[':
        stack.append(string[i])
        now *= 3
    elif string[i] == ')':
        if not stack or stack[-1] != '(':
            isBreak = True
            break
        if string[i-1] == '(':
            total += now
        stack.pop()
        now //= 2
    elif string[i] == ']':
        if not stack or stack[-1] != '[':
            isBreak = True
            break
        if string[i-1] == '[':
            total += now
        stack.pop()
        now //= 3

if isBreak or stack:
    print(0)
else:
    print(total)