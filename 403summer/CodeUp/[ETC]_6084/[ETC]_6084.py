#[기초-종합] 소리 파일 저장용량 계산하기

h, b, c, s =input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

print(round(h*b*c*s/8/1024/1024, 1), 'MB')