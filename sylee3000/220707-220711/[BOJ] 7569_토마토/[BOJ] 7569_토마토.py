from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = []
bfs_queue = deque()
for i in range(H):
    tomato_2 = []
    for j in range(N):
        tomato_1 = list(map(int, input().split()))
        for k in range(M):
            if tomato_1[k] == 1:
                bfs_queue.append((i, j, k, 0))
        tomato_2.append(tomato_1)
    tomato.append(tomato_2)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    res = 0
    while bfs_queue:
        z, x, y, k = bfs_queue.popleft()
        res = max(res, k)
        for i in range(6):
            next_z = z + dz[i]
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_z < H and 0 <= next_x < N and 0 <= next_y < M:
                if tomato[next_z][next_x][next_y] == 0:
                    tomato[next_z][next_x][next_y] = 1
                    bfs_queue.append((next_z, next_x, next_y, k + 1))
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 0:
                    return -1
    return res

print(bfs())
