N = int(input())
A = set(map(int,input().split()))
M = int(input())
M_l = map(int,input().split())
for i in M_l:
    print(1) if i in A else print(0)