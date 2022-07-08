qwerty_number_line = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
qwerty_first_line = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\']
qwerty_second_line = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'"]
qwerty_last_line = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']

while True:
    try:
        w_s = list(input().rstrip())
        c_s = []
        for i in w_s:
            if i == ' ':
                c_s.append(i)
            elif i in qwerty_number_line:
                c_s.append(qwerty_number_line[qwerty_number_line.index(i)-1])
            elif i in qwerty_first_line:
                c_s.append(qwerty_first_line[qwerty_first_line.index(i)-1])
            elif i in qwerty_second_line:
                c_s.append(qwerty_second_line[qwerty_second_line.index(i)-1])
            else:
                c_s.append(qwerty_last_line[qwerty_last_line.index(i)-1])
        print(''.join(c_s))
    except EOFError:
        break
