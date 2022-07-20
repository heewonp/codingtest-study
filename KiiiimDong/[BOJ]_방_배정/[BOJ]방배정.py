n, k = map(int, input().split())  #학생 수, 한 방 최대 인원 수
female = [0] * 1000 # 리스트 초기화
male = [0] * 1000 # 리스트 초기화

for j in range(n):
    s, y = map(int, input().split())  #성별(s), 학년(y)
    #학년별 인원수 체크
    if s == 0:  #여자
        female[y] += 1 # y학년에 숫자 카운트
    else:  #남자
        male[y] += 1 # y학년에 숫자 카운트
    
for j in range(1, 7):
    if female[j] % k == 0:  #인원수 딱 맞게 떨어질 때
        female[j] = female[j] // k # 나눈 몫을 넣는다.
    else: # 안맞아 떨어질 때
        female[j] = (female[j] // k) + 1  #나눈 몫 +1

    if male[j] % k == 0:
        male[j] = male[j] // k
    else:
        male[j] = (male[j] // k) + 1

print(sum(female) + sum(male))
