K = int(input())
sum_l = []
for _ in range(K):
    A = int(input())
    if A == 0:
        sum_l.pop()
    else:
        sum_l.append(A)
print(sum(sum_l))