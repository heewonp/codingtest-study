rome_to_arabic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def r_to_a(r):
    r_reverse = r[::-1]
    result = 0
    recent_value = 0
    for i in r_reverse:
        value = rome_to_arabic[i]
        if recent_value > value:
            result -= value
        else:
            result += value
        recent_value = value
    return result

def a_to_r(a):
    result = ''
    if a >= 1000:
        result += 'M' * (a // 1000)
        a = a % 1000
    if a >= 900:
        result += 'CM'
        a = a - 900
    elif a >= 500:
        result += 'D'
        a = a - 500
    if a >= 400:
        result += 'CD'
        a = a - 400
    elif a >= 100:
        result += 'C' * (a // 100)
        a = a % 100
    if a >= 90:
        result += 'XC'
        a = a - 90
    elif a >= 50:
        result += 'L'
        a = a - 50
    if a >= 40:
        result += 'XL'
        a = a - 40
    elif a >= 10:
        result += 'X' * (a // 10)
        a = a % 10
    if a == 9:
        result += 'IX'
        a = 0
    elif a >= 5:
        result += 'V'
        a = a - 5
    if a == 4:
        result += 'IV'
    else:
        result += 'I' * a
    return result

r1 = input()
r2 = input()
arabic_sum = r_to_a(r1) + r_to_a(r2)
print(arabic_sum)
print(a_to_r(arabic_sum))
