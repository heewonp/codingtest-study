K, N  = map(int,input().split())
K_l = []
for _ in range(K):
    K_l.append(int(input()))
min_range, max_range = 1, max(K_l)
result = 0
while min_range <= max_range:
    answer = (min_range + max_range) // 2
    cut_sum = sum([i // answer for i in K_l])
    if cut_sum >= N:
        result = answer
        min_range = answer + 1
    elif cut_sum < N:
        max_range = answer -1
print(result)