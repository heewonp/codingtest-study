## 덩치
[문제링크](https://www.acmicpc.net/problem/7568)

![덩치1](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EB%8D%A9%EC%B9%98.JPG?raw=true)
![덩치2](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EB%8D%A9%EC%B9%982.JPG?raw=true)

```python
import sys
N = int(sys.stdin.readline())
N_l = []
for _ in range(N):
    N_l.append(list(map(int,sys.stdin.readline().split())))

N_s = ""
for i in range(N):
    grade = 1
    for j in range(N):
        if N_l[i][0] < N_l[j][0] and N_l[i][1] < N_l[j][1]:
            grade += 1
    N_s += str(grade)+" "
print(N_s)
```