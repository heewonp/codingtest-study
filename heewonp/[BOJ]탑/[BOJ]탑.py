import sys
input = sys.stdin.readline

n = int(input())
tower_list = list(map(int,input().split()))
stack = []
res = [0] * n

for i in range(n):
    while stack:
        if tower_list[stack[-1][0]] <= tower_list[i]:
            stack.pop()
        else:
            res[i] = stack[-1][0] + 1
            break

    stack.append([i,tower_list[i]])

for i in res:
    print(i, end=' ')