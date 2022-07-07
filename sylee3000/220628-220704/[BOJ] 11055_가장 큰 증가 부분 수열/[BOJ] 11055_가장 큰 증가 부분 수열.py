N = int(input())
A = list(map(int, input().split()))
dp = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, i):
        if A[j - 1] < A[i - 1]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += A[i - 1]
print(max(dp))
