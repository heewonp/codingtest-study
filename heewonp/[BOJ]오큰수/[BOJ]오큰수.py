import sys
input = sys.stdin.readline

n = int(input())
su_list = list(map(int,input().split()))
stack = []
res = [-1] * n

for i in range(n):
    while stack:
        if su_list[stack[-1]] < su_list[i]:
            res[stack.pop()] = su_list[i]
        else:
            break

    stack.append(i)


# for i in res:
#     print(i, end= ' ')

print(*res)