import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

table_prefix_sum = [[0] * (N + 1) for _ in range(N+1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 and j == 1:
            table_prefix_sum[i][j] = table[i-1][j-1]
        elif i == 1:
            table_prefix_sum[i][j] = table_prefix_sum[i][j-1] + table[i-1][j-1]
        elif j == 1:
            table_prefix_sum[i][j] = table_prefix_sum[i-1][j] + table[i-1][j-1]
        else:
            table_prefix_sum[i][j] = table_prefix_sum[i-1][j] + table_prefix_sum[i][j-1] - table_prefix_sum[i-1][j-1] + table[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(table_prefix_sum[x2][y2] - table_prefix_sum[x2][y1-1] - table_prefix_sum[x1-1][y2] + table_prefix_sum[x1-1][y1-1])
