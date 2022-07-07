import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    a = int(sys.stdin.readline())

    if a == 0:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))