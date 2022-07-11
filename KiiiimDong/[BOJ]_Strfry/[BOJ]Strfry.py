import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    a, b = input().split()
    if sorted(a) == sorted(b):
        print('Possible')
    else:
        print('Impossible')