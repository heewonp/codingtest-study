#[기초-선택실행구조] 월 입력받아 계절 출력하기

n = int(input())

if n//3 == 1:
    print('spring')
elif n//3 == 2:
    print('summer')
elif n//3 == 3:
    print('fall')
else:
    print('winter')
