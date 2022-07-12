from collections import deque
N, K = map(int, input().split())
temp = deque(map(int, input().split()))
temp_left = deque()
temp_part = 0
max_res = -1e9
for i in range(N):
    t = temp.popleft()
    temp_left.append(t)
    temp_part += t
    if i < K - 1:
        continue
    else:
        if i > K - 1:
            temp_part -= temp_left.popleft()
        if temp_part > max_res:
            max_res = temp_part
print(max_res)
