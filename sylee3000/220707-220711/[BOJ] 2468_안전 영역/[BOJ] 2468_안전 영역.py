from collections import deque

N = int(input())
graph = []
max_height = 0
for _ in range(N):
    graph_line = list(map(int, input().split()))
    max_height = max(max(graph_line), max_height)
    graph.append(graph_line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, K, N, visited):
    q = deque()
    q.append((x, y))
    while q:
        a, b = q.popleft()
        if visited[a][b] == 1:
            continue
        else:
            visited[a][b] = 1
            for i in range(4):
                next_a = a + dx[i]
                next_b = b + dy[i]
                if 0 <= next_a < K and 0 <= next_b < K:
                    if graph[next_a][next_b] > N:
                        q.append((next_a, next_b))
max_count = 1                        
for i in range(1, max_height):
    count = 0
    visited = [[0] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, N, i, visited)
                count += 1
    max_count = max(count, max_count)
print(max_count)
