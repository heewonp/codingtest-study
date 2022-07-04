#[기초-선택실행구조] 정수 3개 입력받아 짝수만 출력하기

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a%2 ==0:
    print(a)

if b%2 ==0:
    print(b)

if c%2 ==0:
    print(c)
