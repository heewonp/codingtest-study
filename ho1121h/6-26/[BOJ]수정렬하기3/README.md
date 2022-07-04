# 수정렬하기 3
[문제링크](https://www.acmicpc.net/problem/10989)
```
import sys
N = int(input())
stack = []
for i in range(N):

    a = int(sys.stdin.readline())

    stack.append(a)
stack2 = sorted(stack)

for j in stack2:
    print(j)


```
- 스택 구현하고 저장후 정렬하고 하나씩 출력하면되겠지 했는데 메모리 초과됨

- 메모리 초과 오류를 어떻게 해결해야하나 검색해보니 

1. 그래서 입력값이 10000개 까지 주어질 수 있으니 10000개 만큼의 리스트를 만들어 놓는다.

2. 리스트에 각 요소마다 0을 할당해놓고 입력값을 받을 때마다 그 입력값과 같은 인덱스에 +1씩 해준다.

3. 나중에 입력을 다 받고나면 0보다 큰 요소를 갖는 인덱스들을 찾아서 그 수만큼 인덱스를 출력해주면 된다.

- 리스트를 미리 만들고 인덱스를 찾아서 출력하면 되는 거였다..