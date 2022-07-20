N, M = map(int, input().split())
dp = [0] * (N + 1)
for i in range(N+1):
    if i < M:
        dp[i] = 1
    else:
        dp[i] = (dp[i-1] + dp[i-M]) % 1000000007
print(dp[N])
