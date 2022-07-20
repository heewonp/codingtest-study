from collections import deque
import sys, math
input = sys.stdin.readline

N = int(input())
number_list = deque()
for _ in range(N):
    number_list.append(int(input()))

sub = deque()
for i in range(N-1):
    sub.append(number_list[i+1] - number_list[i])

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

while len(sub) > 1:
    a = sub.popleft()
    b = sub.popleft()
    sub.append(gcd(a, b))
    
gcd_num = sub.popleft()
result = []
result.append(gcd_num)

for i in range(2, int(math.sqrt(gcd_num))+ 1):
    if gcd_num % i == 0:
        result.append(i)
        if (gcd_num // i) not in result:
            result.append(gcd_num // i)
print(*sorted(result))
