N = int(input())
A = list(map(int, input().split()))
dp = [0] * (N + 1)
dp_rev = [0] * (N + 1)
dp_rev[N] = 1
dp_bitonic = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(i):
        if A[i-1] > A[j-1]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
    
for i in range(N - 1, 0, -1):
    for j in range(N, i, -1):
        if A[i-1] > A[j-1]:
            dp_rev[i] = max(dp_rev[i], dp_rev[j])
    dp_rev[i] += 1
    
for i in range(N+1):
    dp_bitonic[i] = dp[i] + dp_rev[i] - 1
print(max(dp_bitonic))
