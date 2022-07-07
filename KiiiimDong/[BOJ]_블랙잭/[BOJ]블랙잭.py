from itertools import combinations
import sys
input = sys.stdin.readline
n ,m = map(int, input().split())
card_list = list(map(int, input().split()))
count_lst = []

for three in combinations(card_list, 3):
    if sum(three) > m:
        # print(three)
        continue
    else:
        # print(three)
        count_lst.append(sum(three))
print(max(count_lst))