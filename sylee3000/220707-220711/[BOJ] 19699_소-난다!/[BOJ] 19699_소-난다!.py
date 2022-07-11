import math

N, M = map(int, input().split())
H = list(map(int, input().split()))
max_H = sum(sorted(H, reverse=True)[:M])

is_prime = [True for _ in range(max_H + 1)]
prime_cow_weight = []
cow_weight = []

for i in range(2, int(math.sqrt(max_H)) + 1):
    if is_prime[i] == True:
        for j in range(2 * i, max_H+1, i):
            is_prime[j] = False
prime = [i for i in range(2, max_H+1) if is_prime[i]]
             
def sum_cow(N, M, len, x):
    if M == len:
        s = sum(cow_weight)
        if s in prime:
            prime_cow_weight.append(s)
        return
    else:
        for i in range(x, N):
            cow_weight.append(H[i])
            sum_cow(N, M, len+1, i+1)
            cow_weight.pop()
    
sum_cow(N, M, 0, 0)
if prime_cow_weight:
    print(*sorted(set(prime_cow_weight)))
else:
    print(-1)
