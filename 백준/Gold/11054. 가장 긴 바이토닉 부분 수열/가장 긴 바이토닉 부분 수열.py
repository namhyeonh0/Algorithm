N = int(input())
A1 = list(map(int,input().split()))
A2 = A1[::-1]

dp1 = [1] * N
dp2 = [1] * N

for i in range(1,N):
    for j in range(i):
        if A1[i] > A1[j]:
            dp1[i] = max(dp1[j]+1,dp1[i])
        if A2[i] > A2[j]:
            dp2[i] = max(dp2[j]+1,dp2[i])

for i in range(N):
    dp1[i] += dp2[N-1-i] - 1
print(max(dp1))