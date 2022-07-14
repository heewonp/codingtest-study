N = int(input())
lst = list(map(int, input().split()))

if len(lst) == 1:
    print('A')
elif len(lst) == 2:
    if lst[0] == lst[1]:
        print(lst[0])
    else:
        print('A')
else:
    if lst[0] == lst[1]:
        if len(set(lst)) == 1:
            print(lst[0])
        else:
            print('B')
    else:
        a = (lst[2] - lst[1]) / (lst[1] - lst[0])
        b = lst[1] - a * lst[0]
        if a != int(a):
            print('B')
        else:
            for i in range(len(lst) - 1):
                if lst[i + 1] != lst[i] * a + b:
                    print('B')
                    break
            else:
                print(int(lst[-1] * a + b))
