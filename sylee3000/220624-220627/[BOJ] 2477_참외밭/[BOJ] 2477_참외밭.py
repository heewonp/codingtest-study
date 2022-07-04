K = int(input())
l = []
for _ in range(6):
    arrow, length = map(int, input().split())
    l.append(length)
w = l.index(max(l))
h = l.index(max(l[(w-1) % 6], l[(w+1) % 6]))
small_w = l[(h+3) % 6]
small_h = l[(w+3) % 6]
print(K * (l[w] * l[h] - small_w * small_h))
