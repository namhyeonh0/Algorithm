n = int(input())
grapes = [0] * 10001
for i in range(1,n+1):
    grapes[i] = int(input())

dp = [0] * 10001
dp[1] = grapes[1]
dp[2] = grapes[1] + grapes[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-2] + grapes[i], dp[i-3] + grapes[i-1] + grapes[i], dp[i-1])

print(dp[n])