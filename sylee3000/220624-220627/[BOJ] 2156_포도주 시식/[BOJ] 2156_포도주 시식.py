import sys
input = sys.stdin.readline

n = int(input())
wine = []
amount = []
for _ in range(n):
    wine.append(int(input()))

if n >= 1:
    amount.append(wine[0])
    if n >= 2:
        amount.append(wine[0] + wine[1])
        if n >= 3:
            amount.append(max(wine[0] + wine[2], wine[1] + wine[2]))
            if n > 3:
                amount.append(max(amount[1], amount[0] + wine[2]) + wine[3])
                for i in range(4, n):
                    amount.append(max(amount[i-2], amount[i-3] + wine[i-1], amount[i-4] + wine[i-1]) + wine[i])
print(max(amount))
