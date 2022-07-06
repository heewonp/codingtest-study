# [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1

[문제링크](https://codeup.kr/problem.php?id=6075)



## 1. 문제설명

정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.




## 2. 문제풀이

```python
n = int(input())
t = 0
while t<=n:
    print(t)
    t+=1
```



