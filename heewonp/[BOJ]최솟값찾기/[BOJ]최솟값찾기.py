from collections import deque
import sys
input = sys.stdin.readline

n,l = map(int,input().split())
arr = list(map(int,input().split()))
d = [0] * n

q = deque()

for i in range(n):
    while q and q[-1][1] > arr[i]:
        q.pop()

    q.append((i, arr[i]))

    while q and i-q[0][0] >= l:
        q.popleft()

    print(q[0][1], end= " ")