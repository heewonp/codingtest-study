N = int(input())
stair_number = [[0] * 10 for _ in range(N + 1)]
stair_number[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if N == 1:
    print(sum(stair_number[1]))
else:
    for i in range(2, N + 1):
        stair_number[i][0] = stair_number[i-1][1]
        for j in range(1, 9):
            stair_number[i][j] = (stair_number[i-1][j-1] + stair_number[i-1][j+1]) % 1000000000
        stair_number[i][9] = stair_number[i-1][8]
    print(sum(stair_number[N]) % 1000000000)
