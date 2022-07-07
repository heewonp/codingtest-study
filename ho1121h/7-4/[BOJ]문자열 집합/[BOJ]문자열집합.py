import sys

a,b = map(int, sys.stdin.readline().split())
c = 0
a_l = []
b_l = []
for i in range(a):
    a_l.append(sys.stdin.readline())

for i in range(b):
    b_l.append(sys.stdin.readline())

for i in b_l:
    if i in a_l:
        c +=1
print(c)
