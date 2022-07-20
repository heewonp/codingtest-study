T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0, 0]
    dp.append(1.5)
    k = 1.5
    for i in range(2, N):
        k += 0.5
        dp.append(dp[-1] + k)
    print(dp[N])
