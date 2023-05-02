def convert_to_python_case(text):
    txt1 = ''
    for i in txt:
        if i.isupper():
            txt1 += '_' + i
        else:
            txt1 += i
    return txt1[1:].lower()


txt = 'ThisIsCamelCased'

print(convert_to_python_case(txt))