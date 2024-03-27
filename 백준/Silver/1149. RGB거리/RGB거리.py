N = int(input())
costs = []
for _ in range(N):
    costs.append(list(map(int,input().split())))

dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0] = costs[0]

for i in range(1,N):
    dp[i][0] = min(costs[i][0] + dp[i-1][1], costs[i][0] + dp[i-1][2])
    dp[i][1] = min(costs[i][1] + dp[i-1][0], costs[i][1] + dp[i-1][2])
    dp[i][2] = min(costs[i][2] + dp[i-1][0], costs[i][2] + dp[i-1][1])

print(min(dp[N-1]))