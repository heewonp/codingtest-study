# [기초-종합] 주사위 2개 던지기

[문제링크](https://codeup.kr/problem.php?id=6080)



## 1. 문제설명

1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
나올 수 있는 모든 경우를 출력해보자.




## 2. 문제풀이

```python
n, m = input().split()
n = int(n)
m = int(m)

for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)

```

