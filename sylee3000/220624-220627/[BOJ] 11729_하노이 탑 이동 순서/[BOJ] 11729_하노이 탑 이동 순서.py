def hanoi_move(N, start, end):
    if N == 1:
        print(start, end)
        return
    else:
        mid = 6 - start - end
        hanoi_move(N-1, start, mid)
        print(start, end)
        hanoi_move(N-1, mid, end)
        
N = int(input())
print(2 ** N - 1)
hanoi_move(N, 1, 3)
