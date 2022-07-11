## 숫자 카드 2
[문제링크](https://www.acmicpc.net/problem/10816)

![숫자 카드 2](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EC%88%AB%EC%9E%90%20%EC%B9%B4%EB%93%9C%202.JPG?raw=true)

```python
# 시간 초과 발생
import sys
N = int(sys.stdin.readline())
N_l = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_l = list(map(int,sys.stdin.readline().split()))

for i in range(len(M_l)):
    if i == len(M_l)-1:
        print(N_l.count(M_l[i]))
    else:
        print(N_l.count(M_l[i]),end=' ')
```

```python
# 다른 방법
import sys
N = int(sys.stdin.readline())
N_l = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_l = list(map(int,sys.stdin.readline().split()))

count = {}
for i in N_l:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for i in M_l:
    result = count.get(i)
    if result == None:
        print(0,end=' ')
    else:
        print(result,end=' ')
```