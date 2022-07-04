## 제로
[문제링크](https://www.acmicpc.net/problem/10773)

![제로1](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EC%A0%9C%EB%A1%9C1.JPG?raw=true)
![제로2](https://github.com/Parksemo/Parksemo/blob/master/image/%5BBOJ%5D%EC%A0%9C%EB%A1%9C2.JPG?raw=true)

```python
K = int(input())
sum_l = []
for _ in range(K):
    A = int(input())
    if A == 0:
        sum_l.pop()
    else:
        sum_l.append(A)
print(sum(sum_l))
```