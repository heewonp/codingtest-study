import sys
input = sys.stdin.readline
n = list(map(int, input().rstrip()))
table = [0] * 1000
for i in range(len(n)):
    table[n[i]] += 1
six_and_nine = table[6]+table[9]   
cnt = 0 # (0~5)
cnt_s = 0 #(6, 9)
cnt_se = 0 #(7, 8)

for i in range(0, 6):
    if table[i] > cnt:
        cnt = 0
        cnt += table[i]
    else:
        pass

for i in range(7, 9):
    if table[i] > cnt_se:
        cnt_se = 0
        cnt_se += table[i]
    else:
        pass

if six_and_nine % 2 != 0:
    cnt_s += (six_and_nine//2 +1)
else:
    cnt_s += six_and_nine//2

print(max(cnt, cnt_s, cnt_se))