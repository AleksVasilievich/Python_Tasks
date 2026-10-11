num = 0
# li = ''
# while num != 2:
#     text = input()
#     num += 1
#     if len(text) == 1:
#         li += ':' + '0' + text
#     else:
#         li += ':' + text
# h1 = li[1:3]
# m1 = li[4:]
# print(li[1:])

li = ''
while num != 4:
    text = input()
    num += 1
    if len(text) == 1:
        li += ':' + '0' + text
    else:
        li += ':' + text
h = li[1:3]
m = li[4:]
hm1 = li[1:6]
print(hm1)
hm2 = li[7:]    # Вместо print(li[7:]) Нужно будет его вывести в конце - print(hm2)

while hm1[0:1] != hm2[0:1] or hm1[3:] != hm2[3:]:
    if hm1[0:1] != hm2[0:1]:
        if hm1[0] == '0':
            h = str(int(hm1[1]) + 1)
            if len(h) == 1:
                h = '0' + h
        else:
            h = str(int(hm1[0:1]) + 1)
    if hm1[3:] != hm2[3:]:
        if hm1[3] == '0':
            m = str(int(hm1[4:]))
            if len(h) == 1:
                h = '0' + h
        else:
            m = str(int(hm1[3:]) + 1)


    print(h + ':' + m)
    hm1 = str(h) + ':' + str(m)

# print(hm2)

# Далее переводим первое время в минуты и второё время в минуты и делаем один цикл.
# Вот тут главный лайфхак! Переводим оба времени в минуты.
# Просто умножаем часы на 60 и прибавляем минуты.
# Теперь у нас два числа, и сразу видно, какое больше.