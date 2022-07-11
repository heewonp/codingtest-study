import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    stack_word = input().split()
    check = stack_word[0]
    if check == 'push':
        stack.append(stack_word[1])

    elif check == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif check == 'size':
        print(len(stack))

    elif check == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif check == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])