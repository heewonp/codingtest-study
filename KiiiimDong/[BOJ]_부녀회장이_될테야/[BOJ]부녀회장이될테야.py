import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):  
    k = int(input())  # 층
    n = int(input())  # 호
    f0 = [x for x in range(1, n+1)]  # 0층 리스트(1부터 n까지)
    for k in range(k):  # 층 수 만큼 반복
        for i in range(1, n):  # 1 ~ n-1까지 (인덱스로 사용) 0호가 없으니깐 
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1]) # 가장마지막의 수를 출력.