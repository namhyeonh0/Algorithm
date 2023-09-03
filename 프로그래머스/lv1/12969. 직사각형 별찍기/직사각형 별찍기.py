a, b = map(int, input().strip().split(' '))
s = ''
for i in range(b):
    for j in range(a):
        s += '*'
    s += '\n'
print(s)