def diff(X, Y):
    count = 0
    sum_list = X + Y
    return 2 * len(set(sum_list)) - (len(X) + len(Y))

a_count, b_count = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(diff(A, B))
