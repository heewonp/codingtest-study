import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    l, n = map(int, input().split())
    ant = []
    for _ in range(n):
        ant.append(int(input()))
    ant_min = 0
    ant_max = 0
    
    for i in ant:
        if ant_min < min(i, l-i):
            ant_min = min(i, l-i)
        if ant_max < max(i, l-i):
            ant_max = max(i, l-i)
    print(ant_min, ant_max)
