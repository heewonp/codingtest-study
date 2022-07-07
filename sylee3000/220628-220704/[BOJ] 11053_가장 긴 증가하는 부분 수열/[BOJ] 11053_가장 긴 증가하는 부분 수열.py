N = int(input())
A = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = 1
for i in range(2, N + 1):
    for j in range(1, i):
        if A[i-1] > A[j-1]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(max(dp))
