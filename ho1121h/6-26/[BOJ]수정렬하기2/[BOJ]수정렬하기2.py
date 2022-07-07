import sys
N = int(input())
stack = []
for i in range(N):

    a = int(sys.stdin.readline())

    stack.append(a)
stack2 = sorted(stack)

for j in stack2:
    print(j)