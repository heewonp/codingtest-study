import sys
N = int(sys.stdin.readline())
c_l = []
for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    c_l.append([y,x])

c_l = sorted(c_l)

for i in c_l:
    print(i[1],i[0])