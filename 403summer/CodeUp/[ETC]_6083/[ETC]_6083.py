#[기초-종합] 빛 섞어 색 만들기

r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j, end=" ")
            print(k)
print(r*g*b)
