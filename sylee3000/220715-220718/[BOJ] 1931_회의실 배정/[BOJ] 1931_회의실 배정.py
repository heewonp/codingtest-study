from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N):
    start, end = map(int, input().split())
    time.append((start, end))
time.sort(key = lambda x : (x[0], x[1]))
time = deque(time)

start, end, count = 0, 0, 0
while time:
    a, b = time.popleft()
    if a < end:
        if b < end:
            end = b
    else:
        count += 1
        start = a
        end = b
print(count)
