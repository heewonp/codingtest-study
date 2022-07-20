'''import  sys
from queue import Queue 

N = int(sys.stdin.readline()) # 반복횟수 입력
que = Queue()
for _ in range(N): 
    M = sys.stdin.readline().split() # 명령어 입력
    o = M[0] #명령어는 무조건 앞에 옴

    if o == 'push': 
        value = M[1] # 밸류값
        que.put(value) # 큐에 추가

    elif o == 'pop':
        if que.qsize() == 0:
            print(-1)
        else:
            print(que.get())

    elif o == 'size':
        print(que.qsize())

    elif o == 'empty':
        if que.empty() =='True':
            print(1)
        elif que.empty() =='False':
            print(0)
    elif o == 'front': # 제일 앞 숫자 출력
        if que.qsize() == 0 :
            print(-1)
        else:
            q_f= que
            print(q_f.get())
    elif o == 'back': # 제일 뒤 숫자 출력
        if que.qsize() ==0 :
            print(-1)
        else:
            q_b=que
            print(q_b.get())
'''
#print(que.qsize())
#########
'''from sys import stdin
input()
s, com= [], stdin.readlines()
cnt = 0
for x in com:
    c = x.split()
    if c[0] == "push":
        s.append(c[1])
    elif c[0] == 'pop':
        if len(s) > cnt:
            print(s[cnt])
            cnt += 1
        else: print(-1)
    elif c[0] == 'size':
        print(len(s)-cnt)
    elif c[0] == 'empty':
        if len(s) == cnt :
            print(1)
            cnt = 0
            s = []
        else: print(0)
    elif c[0] == 'front':
        if len(s) > cnt: print(s[cnt])
        else: print(-1)
    elif c[0] == 'back':
        if len(s) > cnt: print(s[-1])
        else: print(-1)'''

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

q = deque([]) #리스트 구현

for _ in range(n):
    query = input().split()
    if query[0] == 'push':
            q.append(query[1]) #푸쉬 다음 숫자를 추가
    elif query[0] == 'pop':
        if len(q):
            print(q.popleft()) # 선입 선출로 앞에 숫자 뽑아오기
        else:
            print(-1) # 아니면 -1 출력
    elif query[0] == 'size':
        print(len(q)) # 크기 출력
    elif query[0] == 'empty':
        if len(q): #크기 측정이 가능하면 0 
            print(0)
        else:
            print(1) # 아니면 1
    elif query[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif query[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)