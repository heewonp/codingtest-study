from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
picture = []
for _ in range(N):
    picture_line = list(input())
    picture.append(picture_line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(a, b, count):
    q = deque()
    color = picture[a][b]
    q.append((a, b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y] and picture[next_x][next_y] == color:
                    visited[next_x][next_y] = True
                    q.append((next_x, next_y))

count, count_RG = 0, 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            bfs(i, j, count)
            
for i in range(N):
    for j in range(N):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'
visited = [[False] * N for _ in range(N)]
    
for i in range(N):
    for j in range(N):            
        if not visited[i][j]:
            count_RG += 1
            bfs(i, j, count_RG)

print(count, count_RG)
