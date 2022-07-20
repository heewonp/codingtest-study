from collections import deque

N, K = map(int, input().split())
visited = [1e5] * 100001
min_time = 2e5
count = 0

q = deque()
q.append((N, 0))
while q:
    a, time = q.popleft()
    if a == K:
        if time < min_time:
            min_time = time
            count = 1
        elif time == min_time:
            count += 1
    if visited[a] >= time and time < min_time:
        visited[a] = time
        if a < 100000:
            q.append((a + 1, time + 1))
        if a > 0:
            q.append((a - 1, time + 1))
        if a <= min(50000, K):
            q.append((a * 2, time + 1))
print(min_time)
print(count)
