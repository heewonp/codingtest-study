import  sys
from queue import Queue # 큐 라이브러리 -> 사용안해도될듯

N = int(sys.stdin.readline()) # 반복횟수 입력
que = [] # 큐를 받을 리스트
for _ in range(N): 
    M = sys.stdin.readline().split() # 명령어 입력
    o = M[0] #명령어는 무조건 앞에 옴

    if o == 'push': 
        value = M[1] # 밸류값
        que.append(value) # 큐에 추가

    elif o == 'pop':
        if len(que) ==0:
            print(-1)
        else:
            print(que.pop(0)) # pop 으로 제일 앞에 있는 숫자 꺼냄

    elif o == 'size':
        print(len(que))

    elif o == 'empty':
        if len(que)==0: # 크기가 0 이면 1출력
            print(1)
        else:
            print(0)

    elif o == 'front': # 제일 앞 숫자 출력
        if len(que) == 0 :
            print(-1)
        else:
            print(que[0])
    elif o == 'back': # 제일 뒤 숫자 출력
        if len(que) == 0 :
            print(-1)
        else:
            print(que[-1])

