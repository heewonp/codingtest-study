import math

N = int(input())
ring = list(map(int, input().split()))
ring_st = ring[0]
ring = ring[1:]

for i in ring:
    print(ring_st//math.gcd(ring_st, i), i//math.gcd(ring_st, i), sep='/')
