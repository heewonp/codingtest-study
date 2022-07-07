## 카드2
[문제링크](https://www.acmicpc.net/problem/2164)

![카드2](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EC%B9%B4%EB%93%9C2.JPG?raw=true)

```python
# 시간초과 발생 코드
import sys
N = int(sys.stdin.readline())
N_l = list(range(N,0,-1))
while True:
    if len(N_l) == 1:
        break
    N_l.pop()
    N_l.insert(0,N_l.pop())
print(N_l[0])
```

```python
import sys
import collections
N = int(sys.stdin.readline())
N_l = collections.deque(list(range(N,0,-1)))
while True:
    if len(N_l) == 1:
        break
    N_l.pop()
    N_l.rotate(1)
print(N_l[0])
```

