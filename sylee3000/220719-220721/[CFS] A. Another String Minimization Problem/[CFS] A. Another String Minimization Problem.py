import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    s = ['B'] * m
    for i in a:
        k1, k2 = i - 1, m - i
        if k1 < k2:
            if s[k1] == 'B':
                s[k1] = 'A'
            else:
                s[k2] = 'A'
        else:
            if s[k2] == 'B':
                s[k2] = 'A'
            else:
                s[k1] = 'A'
    print(*s, sep='')
