from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    count = 0
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        
        while q:
            x, y = q.popleft()
            if graph[x][y] == 0:
                continue
            graph[x][y] = 0
            for i in range(4):
                next_x = x+dx[i]
                next_y = y+dy[i]
                if 0 <= next_x < N and 0 <= next_y < M:
                    if graph[next_x][next_y] == 1:
                        q.append((next_x, next_y))
                    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
