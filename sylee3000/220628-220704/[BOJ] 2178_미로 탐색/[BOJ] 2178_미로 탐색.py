from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(input()))

queue = deque([(0, 0)])
maze[0][0] = 1

while queue:
    x, y = queue.popleft()
    if x == N-1 and y == M-1:
        print(maze[x][y])
        break
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
            next_x = x + dx[i]
            next_y = y + dy[i]
            if maze[next_x][next_y] == '1':
                maze[next_x][next_y] = maze[x][y] + 1
                queue.append((next_x, next_y))
