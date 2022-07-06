# [기초-종합] 짝수 합 구하기

[문제링크](https://codeup.kr/problem.php?id=6077)



## 1. 문제설명

정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.




## 2. 문제풀이

```python
n = int(input())
s = 0
for i in range(1,n+1):
    if i%2 == 0:
        s += i
print(s)
```



