#[기초-종합] 수 나열하기1

a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

for i in range(1,n):
    a +=d

print(a)    

