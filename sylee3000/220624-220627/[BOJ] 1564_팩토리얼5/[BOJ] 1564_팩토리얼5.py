N = int(input())
res = 1
for i in range(1, N+1):
    res *= i
    while res % 10 == 0:
        res /= 10
    res = res % 1000000000000
print(str(int(res))[-5:])
