#[기초-종합] 주사위 2개 던지기

n, m = input().split()
n = int(n)
m = int(m)

for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)
