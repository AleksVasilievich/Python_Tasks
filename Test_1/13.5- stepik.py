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
    
txt = 'sjdflksjflksdjflsdjk sdlfhsdjfE#R#$$#R !!!!! sdjfnsdjkfnsd kjcvadsk'
# txt = input()

print(is_palindrome(txt))