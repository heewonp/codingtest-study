T = int(input())

def divide_by_twothree(n, two, res):
    if n == 0:
        return
    else:
        if n % 2 == 0:
            divide_by_twothree(n // 2, two + 1, res)
        else:
            i = 1
            while n >= 3 ** i:
                i += 1
            n -= 3 ** (i - 1)
            res.append((two, i - 1))
            divide_by_twothree(n, two, res)

for _ in range(T):
    N = int(input())
    res = []
    divide_by_twothree(N, 0, res)
    print(len(res))
    for i in res:
        print(*i)
