import sys
import collections
N = int(sys.stdin.readline())
N_l = collections.deque(list(range(N,0,-1)))
while True:
    if len(N_l) == 1:
        break
    N_l.pop()
    N_l.rotate(1)
print(N_l[0])