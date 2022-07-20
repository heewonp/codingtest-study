#[기초-종합] 그림 파일 저장용량 계산하기

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = a*b*c/8/1024/1024
print('%.2f'%d, 'MB')

