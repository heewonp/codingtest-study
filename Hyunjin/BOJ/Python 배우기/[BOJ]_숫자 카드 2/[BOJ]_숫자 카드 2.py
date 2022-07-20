import sys
N = int(sys.stdin.readline())
N_l = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_l = list(map(int,sys.stdin.readline().split()))

count = {}
for i in N_l:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for i in M_l:
    result = count.get(i)
    if result == None:
        print(0,end=' ')
    else:
        print(result,end=' ')