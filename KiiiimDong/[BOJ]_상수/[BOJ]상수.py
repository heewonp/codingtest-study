import sys
input = sys.stdin.readline
n, m = input().split()
if int(n[::-1])>=int(m[::-1]):
    print(n[::-1])
else:
    print(m[::-1])
