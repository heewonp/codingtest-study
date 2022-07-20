## 수찾기
[문제링크](https://www.acmicpc.net/problem/1920)

![수찾기](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EC%88%98%EC%B0%BE%EA%B8%B0.JPG?raw=true)

```python
N = int(input())
A = set(map(int,input().split())) #list로 하면 시간초과 발생
M = int(input())
M_l = map(int,input().split())
for i in M_l:
    print(1) if i in A else print(0)
```