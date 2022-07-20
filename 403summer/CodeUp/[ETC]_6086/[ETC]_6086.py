#[기초-종합] 거기까지! 이제 그만~

from calendar import c


n = int(input())
s = 0
c = 0
while True:
    s+=c
    c+=1
    if s>=n:
        break
print(s)