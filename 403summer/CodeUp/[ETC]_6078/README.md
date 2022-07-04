# [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기

[문제링크](https://codeup.kr/problem.php?id=6078)



## 1. 문제설명

영문 소문자 'q'가 입력될 때까지
입력한 문자를 계속 출력하는 프로그램을 작성해보자.




## 2. 문제풀이

```python
while True:

    x = input()
    print(x)

    if x=='q':
        break 
```


