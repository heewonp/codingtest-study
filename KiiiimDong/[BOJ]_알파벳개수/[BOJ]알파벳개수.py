S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(alphabet)):
    print(S.count(alphabet[i]), end = ' ')