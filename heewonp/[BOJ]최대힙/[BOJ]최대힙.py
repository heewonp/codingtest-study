import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            # print(0)
            print(-heapq.heappop(heap))
        else:
            # print(-heapq.heappop(heap))
            print(0)
    else:
        heapq.heappush(heap,-x)