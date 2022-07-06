import sys
input = sys.stdin.readline
n=int(input())

for i in range(n):
   R,S=input().split()
    
   for j in S:
      print(j*int(R), end='')
   print()
