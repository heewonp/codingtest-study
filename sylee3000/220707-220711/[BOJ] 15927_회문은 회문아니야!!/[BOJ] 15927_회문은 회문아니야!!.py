str_list = list(input())
if len(set(str_list)) == 1:
    print(-1)
elif str_list != str_list[::-1]:
    print(len(str_list))
else:
    print(len(str_list)-1)
