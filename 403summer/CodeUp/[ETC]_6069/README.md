# [기초-선택실행구조] 평가 입력받아 다르게 출력하기

[문제링크](https://codeup.kr/problem.php?id=6069)



## 1. 문제설명

평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

평가 내용
평가 : 내용
A : best!!!
B : good!!
C : run!
D : slowly~
나머지 문자들 : what?




## 2. 문제풀이

```python
n = input()

if n == 'A':
    print('best!!!')
elif n == 'B':
    print('good!!')
elif n == 'C':
    print('run!')
elif n == 'D':
    print('slowly~')
else:
    print('what?')
```





