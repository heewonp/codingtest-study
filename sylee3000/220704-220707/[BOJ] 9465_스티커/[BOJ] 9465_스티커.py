from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    list1 = deque(map(int, input().split()))
    list2 = deque(map(int, input().split()))
    
    max_score = []
    for i in range(n):
        a = list1.popleft()
        b = list2.popleft()
        if i == 0:
            max_score.append((a, b))
        elif i == 1:
            max_score.append((max_score[-1][1] + a, max_score[-1][0] + b))
        else:
            max_a = max(max_score[-1][1] + a, max(max_score[-2]) + a)
            max_b = max(max_score[-1][0] + b, max(max_score[-2]) + b)
            max_score.append((max_a, max_b))
    print(max(max_score[-1]))
