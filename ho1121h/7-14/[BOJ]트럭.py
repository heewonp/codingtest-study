import sys

n, w, l = map(int, sys.stdin.readline().split())  # 트럭, 길이, 무게

트럭 = list(map(int, sys.stdin.readline().split()))  # ex )  [7,4,5,6]

다리 = [0] * w  # 길이만큼 생성
time = 0  # 길이한칸씩 이동할때마다 시간을 구하기 위함

while 다리:
    time += 1  # 한칸당 1 카운트
    다리.pop(0)  # 다리의칸을 하나씩 줄임

    if 트럭:
        if sum(다리) + 트럭[0] <= l:  # 다리위 트럭의 무게가 l보다 작아야한다.
            다리.append(트럭.pop(0))  # 제일앞 트럭이 다리위로 올라감
        else:
            다리.append(0)
print(time)

