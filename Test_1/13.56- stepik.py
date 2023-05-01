'''Напишите функцию is_palindrome(text), которая принимает в качестве аргумента
строку text и возвращает значение True если указанный текст является
палиндромом и False в противном случае.
Примечание 1. Палиндром – это строка, которая читается одинаково 
в обоих направлениях
Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми,
а также игнорируйте пробелы, а также символы , . ! ? -.
Примечание 3. Следующий программный код:

print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))
'''

def is_palindrome(text):
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
    
    if txt3[:num] == txt3[:(num - 1): -1]:
        return True, len(txt2), txt2, txt3[:num], txt3[:(num - 1): -1]

    return False, len(txt2), txt2, txt3[:num], txt3[:(num - 1): -1]

    # или вместо предидущих трёх строк (будет True или False)
    # return txt3[:num] == txt3[:(num - 1): -1]
    
txt = 'sjdflksjflksdjflsdjk sdlfhsdjfE#R#$$#R !!!!! sdjfnsdjkfnsd kjcvadsk'
# txt = input()

print(is_palindrome(txt))