#[기초-선택실행구조] 점수 입력받아 평가 출력하기

n = int(input())

if n>=90:
    print('A')
else:
    if n>=70:
        print('B')
    else:
        if n>=40:
            print('C')
        else:
            print('D')
