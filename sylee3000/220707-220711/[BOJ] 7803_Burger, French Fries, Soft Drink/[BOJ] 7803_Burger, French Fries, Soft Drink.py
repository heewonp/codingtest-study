def bin_coef(n, k):
    res = 1
    for i in range(n, n-k, -1):
        res = res * i 
    for i in range(1, k+1):
        res = res // i
    return res

while True:
    try:
        N, order_list = input().split()
        order = []
        B = S = F = 0
        for i in order_list:
            if i == 'B':
                B += 1
            elif i == 'S':
                S += 1
            else:
                F += 1
            if B == S == F:
                order.append(B)
                B = S = F = 0
        if B != 0 or S != 0 or F != 0:
            print("Impossible")
        else:
            res = bin_coef(int(len(order)) - 1, int(N)- 1)
            if res > 0:
                print(res)
            else:
                print("Impossible")
    except EOFError:
        break
