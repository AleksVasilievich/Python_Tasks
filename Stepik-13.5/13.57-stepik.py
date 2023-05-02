'''
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы
с необычным паролем.
Действительный пароль BEEGEEK банка имеет вид a:b:c, 
где a, b и c – натуральные числа. Поскольку основатель BEEGEEK 
фанатеет от математики, то он решил:
число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает 
в качестве аргумента строковое значение пароля password 
и возвращает значение True если пароль является действительным паролем 
BEEGEEK банка и False в противном случае.
'''

def is_even(num):
    return num % 2 == 0

def is_prime(num):
    b = 0
    for i in range(1, num + 1):
        if num % i == 0:
            b = b + 1
    return b == 2

def is_palindrome(txt):
    txt1 = txt.lower()
    txt2 = ''
    txt3 = ''
    for i in txt1:
        if i != '.' and i != '!' and i != '?' and i != '-' and i != ' ' and i != ',':
            txt2 = txt2 + i
    num = len(txt2) // 2
    if len(txt2) % 2 != 0:
        txt3 = txt2[:num] + txt2[(num + 1):]
    else:
        txt3 = txt2
    
    return txt3[:num] == txt3[:(num - 1): -1]


def is_valid_password(password):
    a = ''; b = ''; c = ''
    n1 = password.find(':')
    n2 = password.rfind(':')
    # n3 = password.count(':')
    a = password[:n1]
    b = password[n1 + 1 :n2]
    c = password[n2 + 1:]
    if password.count(':') == 2:
        return is_palindrome(a) and is_prime(int(b)) and is_even(int(c))
    else:
        return False    


psw = '15551:7:290'
# psw = input()

print(is_valid_password(psw))