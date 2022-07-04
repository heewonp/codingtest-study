from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
graph = []
count_list = []
for _ in range(N):
    graph_line = list(input())
    graph.append(graph_line)

def bfs(x, y):
    count = 0
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        if graph[x][y] == '0':
            continue
        graph[x][y] = '0'
        count += 1
        for i in range(4):
            next_x = x+dx[i]
            next_y = y+dy[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                if graph[next_x][next_y] == '1':
                    q.append((next_x, next_y))
    return count
                
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            count_list.append(bfs(i, j))
print(len(count_list))
for i in sorted(count_list):
    print(i)
