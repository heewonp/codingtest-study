import sys
input = sys.stdin.readline

N = int(input())
ramen = list(map(int, input().split()))

total_cost = 0

for i in range(N-2):
    if ramen[i+1] > ramen[i+2]:
        buy_2 = min(ramen[i], ramen[i+1] - ramen[i+2])
        ramen[i] -= buy_2
        ramen[i+1] -= buy_2
        total_cost += buy_2 * 5
        
        buy_3 = min(ramen[i], ramen[i+1], ramen[i+2])
        ramen[i] -= buy_3
        ramen[i+1] -= buy_3
        ramen[i+2] -= buy_3
        total_cost += buy_3 * 7
        
        total_cost += ramen[i] * 3
        ramen[i] = 0
    else:
        buy_3 = min(ramen[i], ramen[i+1], ramen[i+2])
        ramen[i] -= buy_3
        ramen[i+1] -= buy_3
        ramen[i+2] -= buy_3
        total_cost += buy_3 * 7
        
        total_cost += ramen[i] * 3
        ramen[i] = 0
        
remain_buy_2 = min(ramen[N-2], ramen[N-1])
total_cost += remain_buy_2 * 5
ramen[N-2] -= remain_buy_2
ramen[N-1] -= remain_buy_2

total_cost += max(ramen[N-2], ramen[N-1]) * 3

print(total_cost)
