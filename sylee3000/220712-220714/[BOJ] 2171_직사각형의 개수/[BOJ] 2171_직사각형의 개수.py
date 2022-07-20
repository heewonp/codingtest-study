from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
p = []
for _ in range(N):
    x, y = map(int, input().split())
    p.append((x, y))
p.sort(key=lambda x:(x[0], x[1]))
    
c = Counter(p)
ans = 0
for i in range(N):
    x1, y1 = p[i]
    for j in range(i+1, N):
        x2, y2 = p[j]
        if x1 != x2 and y1 != y2 and x1 < x2 and y1 < y2:
            if c[(x1, y2)] and c[(x2, y1)]:
                ans += 1
print(ans)
