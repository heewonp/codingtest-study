#[기초-종합] 수 나열하기2

a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)

for i in range(1,n):
    a*=r
print(a)