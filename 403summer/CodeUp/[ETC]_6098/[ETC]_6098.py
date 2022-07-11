#[기초-리스트] 성실한 개미

ant = []
for i in range(10):
    ant.append(list(map(int,input().split())))

x = 1
y = 1
ant[x][y] = 9
while True:
    if ant[x][y+1] == 0:
        y+=1
        ant[x][y] = 9

    elif ant[x][y+1] == 2:
        y+=1
        ant[x][y] = 9
        break

    elif ant[x][y+1] == 1:
        if ant[x+1][y] == 1:
            break
        elif ant[x+1][y] == 2:
            x+=1
            ant[x][y] = 9
            break
        elif ant[x+1][y] == 0:
            x+=1
            ant[x][y] = 9
            
for i in range(10):
    for j in range(10):
        if j == 9:
            print(ant[i][j])
        else:
            print(ant[i][j], end = ' ')