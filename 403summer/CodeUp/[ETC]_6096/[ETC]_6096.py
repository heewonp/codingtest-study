#[기초-리스트] 바둑알 십자 뒤집기

d = [input().split() for i in range(19)]

for i in range(19):
    for j in range(19):
        d[i][j] = int(d[i][j])

n = int(input())
for i in range(n):
    x, y =input().split()
    x = int(x)-1
    y = int(y)-1
    for j in range(19):
        
        if d[j][y] == 0:
            d[j][y] = 1

        else:
            d[j][y] = 0
        
        if d[x][j] == 0:
            d[x][j] = 1

        else:
            d[x][j] = 0

for i in range(19):
    for j in range(19):
        if j == 18:
            print(d[i][j])
        else:
            print(d[i][j], end=' ')