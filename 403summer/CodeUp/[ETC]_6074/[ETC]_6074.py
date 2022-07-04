#[기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기

c = ord(input())
t = ord('a')
while t<=c:
    print(chr(t), end=' ')
    t+=1
