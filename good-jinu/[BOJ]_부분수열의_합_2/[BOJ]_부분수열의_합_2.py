import sys

input = sys.stdin.readline

MAX_NUM = 20000000
numcount = [0 for _ in range(MAX_NUM * 2 + 1)]

N, S = map(int, input().split())
numlst = list(map(int, input().split()))
ans = [0]
iscounted = [False]


def numtoind(num):
    return MAX_NUM + num


def countnum(comb, start, end, callersum):
    if comb == 1:
        for i in range(start, end):
            if iscounted[0]:
                ans[0] += numcount[numtoind(S - callersum - numlst[i])]
            else:
                numcount[numtoind(callersum + numlst[i])] += 1
    else:
        for i in range(start, end - comb + 1):
            newsum = callersum + numlst[i]
            countnum(comb - 1, i + 1, end, newsum)


half_ind = N // 2
numcount[numtoind(0)] = 1
for a in range(1, half_ind + 1):
    countnum(a, 0, half_ind, 0)
ans[0] += numcount[numtoind(S)]
iscounted[0] = True
for a in range(1, N - half_ind + 1):
    countnum(a, half_ind, N, 0)
if S == 0:
    ans[0] -= 1

print(ans[0])