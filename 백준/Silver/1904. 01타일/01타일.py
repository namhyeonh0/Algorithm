N = int(input())

a1 = 1
a2 = 2
answer = 0
for _ in range(N-2):
    answer = a1 + a2
    if answer >= 15746:
        answer %= 15746
    a1 = a2
    a2 = answer

if N == 1:
    answer = 1
elif N == 2:
    answer = 2

print(answer)