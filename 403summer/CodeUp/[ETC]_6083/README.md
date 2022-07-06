# [기초-종합] 빛 섞어 색 만들기

[문제링크](https://codeup.kr/problem.php?id=6083)



## 1. 문제설명

빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.

빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,
주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자. 

**모니터, 스마트폰과 같은 디스플레이에서 각 픽셀의 색을 만들어내기 위해서 r, g, b 색을 조합할 수 있다.
**픽셀(pixel)은 그림(picture)을 구성하는 셀(cell)에서 이름이 만들어졌다.




## 2. 문제풀이

```python
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j, end=" ")
            print(k)
print(r*g*b)
```

