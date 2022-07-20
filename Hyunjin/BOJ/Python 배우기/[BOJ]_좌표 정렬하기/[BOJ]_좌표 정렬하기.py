import sys
N = int(sys.stdin.readline())
c_l = []
for _ in range(N):
    c_l.append(list(map(int,sys.stdin.readline().split())))

c_l = sorted(c_l)

for i in c_l:
    print(i[0],i[1])