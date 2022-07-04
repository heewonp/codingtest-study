import  sys

N = int(sys.stdin.readline()) # 오류를 최소화하기위해 sys 사용

stack = [] # 스택 구현

for _ in range(N): #N번의 명령이 주어짐
    M = sys.stdin.readline().split() # 명령어가 입력됨
    o = M[0] #명령어는 무조건 앞에 옴

    if o == 'push':
        value = M[1]
        stack.append(value)

    elif o == 'pop':
        if len(stack) ==0:
            print(-1)
        else:
            print(stack.pop())

    elif o == 'size':
        print(len(stack))

    elif o == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    elif o == 'top':
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack[-1])


