S = input()
part_string = []
for i in range(1, len(S) + 1):
    for j in range(len(S) - i + 1):
        part_string.append(S[j:j+i])
part_string = set(part_string)
print(len(part_string))
