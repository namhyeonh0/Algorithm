n = int(input())
scores = [0]
for _ in range(n):
    scores.append(int(input()))

if n <= 2:
    print(sum(scores))
else:
    dp = [0] * (n+1)
    dp[1] = scores[1]
    dp[2] = dp[1] + scores[2]
    for i in range(3,n+1):
        dp[i] = max(scores[i] + dp[i-2], scores[i] + scores[i-1] + dp[i-3])
    print(dp[n])