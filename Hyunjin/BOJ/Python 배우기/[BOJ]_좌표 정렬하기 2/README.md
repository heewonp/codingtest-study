## 좌표 정렬하기 2
[문제링크](https://www.acmicpc.net/problem/11650)

![좌표 정렬하기 2](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EC%A2%8C%ED%91%9C%20%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0%202.JPG?raw=true)

```python
## 맞는 것 같은데 틀린 코드
import sys
N = int(sys.stdin.readline())
c_l = []
for _ in range(N):
    c_l.append(list(map(int,sys.stdin.readline().split())))

c_l = sorted(c_l, key=lambda c_l : c_l[1])

for i in c_l:
    print(i[0],i[1])
```

```python
# 새롭게 작성한 코드
import sys
N = int(sys.stdin.readline())
c_l = []
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    c_l.append([y,x])

c_l = sorted(c_l)

for i in c_l:
    print(i[1],i[0])
```