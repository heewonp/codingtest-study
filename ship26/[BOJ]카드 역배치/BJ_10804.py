import sys

card= [i for i in range(1,21)]  #카드생성

#reverse_card = list(reversed(card[(5 - 1):(10 - 1)]))

for _ in range(0,10):
    a,b = map(int,sys.stdin.readline().split())  #a,b 얻기
    reverse_card= list(reversed(card[(a - 1):(b)]))  #역순정렬카드(a,b)

    for v in range(0,len(reverse_card)):  #역순정렬된카드를 for문동안 원래 카드에배치
        card[a-1+v]=reverse_card[v]

for j in card:   #출력
    if j != len(card):
        print(f'{j} ',end='')

    else:
        print(j)
