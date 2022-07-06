import sys
N = int(input()) # 정수입력 갯수 설정
stack = [0] * 10001 # 리스트 미리 구현
for i in range(N):

    a = int(sys.stdin.readline()) # 정수 하나씩 입력
    stack[a] = stack[a] + 1 # 각 정수자리의 인덱스에 스택쌓기

#stack2 = sorted(stack)

for j in range(10001):
    if stack[j] !=0:
        for k in range(stack[j]):
            print(j)