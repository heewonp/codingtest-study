import sys
input = sys.stdin.readline

k = int(input())
stack = []

for i in range(k):
    k_stack = int(input())
    if k_stack == 0:
        stack.pop()
    else:
        stack.append(k_stack)

print(sum(stack))