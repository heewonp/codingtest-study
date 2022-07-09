N = int(input())
factor = [9, 3, 7]
case = 1
for _ in range(N):
    id = list(input())
    id = id[::-1]
    index = 0
    checksum = 0
    question_index = 0
    for i in id:
        if i == '?':
            question_index = index
        else:
            checksum += int(i) * factor[index]
        index = (index + 1) % 3
    id = id[::-1]
    for i in range(10):
        if (checksum + i * factor[question_index]) % 10 == 0:
            for j in range(len(id)):
                if id[j] == '?':
                    id[j] = str(i)
            print(f'Scenario #{case}:')
            print(''.join(id))
            print()
            case += 1
