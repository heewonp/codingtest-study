import sys
input = sys.stdin.readline
n, m = map(int, input().split())
space_list = []
for i in range(n):
    space_list.append(input().rstrip())
repair = []

for i in range(n-7): # 행 인덱스 제한
    for j in range(m-7): # 열 인덱스 제한
        first_W = 0 # 첫 칸이 하얀색일때
        first_B = 0 # 첫 칸이 검은색일때
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0: # 짝수일때(처음이랑 같아야함)
                    if space_list[k][l] != 'W':
                        first_W += 1 
                    if space_list[k][l] != 'B':
                        first_B += 1 # 
                else: # 짝수 아닐때(처음이랑 달라야함)
                    if space_list[k][l] != 'B':
                        first_W += 1
                    if space_list[k][l] != 'W':
                        first_B += 1
        repair.append(first_W)
        repair.append(first_B)

print(min(repair))