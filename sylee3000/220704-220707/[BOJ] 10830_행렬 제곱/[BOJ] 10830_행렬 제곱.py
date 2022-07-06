import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

def matrix_multiple(A, B, N):
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % 1000
    return C           
    
def matrix_sq(A, B, N):
    if B == 1:
        return A
    if B % 2 == 0:
        C = matrix_sq(A, B // 2, N)
        return matrix_multiple(C, C, N)
    else:
        C = matrix_sq(A, B-1, N)
        return matrix_multiple(C, A, N)
    
res = matrix_sq(A, B, N)

for i in range(N):
    for j in range(N):
        print(res[i][j] % 1000, end=' ')
    print()
