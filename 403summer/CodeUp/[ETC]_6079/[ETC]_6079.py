#[기초-종합] 언제까지 더해야 할까?

n = int(input())
p = 0
m = 0
while True:
    p += 1
    m += p
    if n<=m:
        print(p)
        break
