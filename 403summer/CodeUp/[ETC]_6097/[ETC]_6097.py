#[기초-리스트] 설탕과자 뽑기

h, w = map(int,input().split())

list = [[0 for i in range(w)] for i in range(h)]

n = int(input())
for i in range(n):
    l, d, x, y = map(int,input().split())
    for j in range(l):
        if d == 0:
            list[x-1][y-1+j] = 1
        else:
            list[x-1+j][y-1] = 1

for i in range(h):
    for j in range(w):
        if j+1 == w:
            print(list[i][j])
        else:
            print(list[i][j], end=' ')
