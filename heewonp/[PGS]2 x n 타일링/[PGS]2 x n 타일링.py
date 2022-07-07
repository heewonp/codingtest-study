def solution(n):
    # 경우의 수
    dp = [0] * (n)
    # dp 가로세로 길이 설정
    dp[0],dp[1] = 1,2
    for i in range(2,n):
        dp[i] = (dp[i-1]+dp[i-2]) % 1000000007
    return dp[n-1]