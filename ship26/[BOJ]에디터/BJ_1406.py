import sys


리스트1= list(sys.stdin.readline().rstrip())
리스트2 = list()

n = int(sys.stdin.readline().rstrip())   #명령어 갯수
for i in range(0, n):
    명령 = list(sys.stdin.readline().split())  #명령어받기
    if 명령[0] == 'L' and 리스트1:
        리스트2.append(리스트1.pop())  #좌로 커서옮길시 우측리스트로 원소 옮기기
    elif 명령[0] == 'D' and 리스트2:  #우로 커서 옮길시 좌측 리스트로 원소 옮기기
        리스트1.append(리스트2.pop())
    elif 명령[0] == 'B' and 리스트1:  #원소 삭제
        리스트1.pop()
    elif 명령[0] == 'P':  #원소 추가
        리스트1.append(명령[1])

print(''.join(리스트1) + ''.join(list(reversed(리스트2))))  #출력
