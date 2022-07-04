import sys #sys 사용

t = int(input()) # 반복횟수 입력
for i in range(t):# 반복횟수크기 만큼 반복
    a, b = map(int, sys.stdin.readline().split())# 정수 2개를 받음
    print(a + b)# 정수 2개를 더한값