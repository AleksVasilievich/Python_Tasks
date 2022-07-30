# Создайте программу для игры в ""Крестики-нолики"".


from unicodedata import name

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
vic = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
       [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def print_field():
    print(field[0], end='  ')
    print(field[1], end='  ')
    print(field[2])
    print(field[3], end='  ')
    print(field[4], end='  ')
    print(field[5])
    print(field[6], end='  ')
    print(field[7], end='  ')
    print(field[8])


def wey_field(wey, name):
    num = field.index(wey)
    field[num] = name


def take_line():
    prize = ''

    for i in vic:
        if field[i[0]] == 'X' and field[i[1]] == 'X' and field[i[2]] == 'X':
            prize = 'X'
        if field[i[0]] == 'O' and field[i[1]] == 'O' and field[i[2]] == 'O':
            prize = 'O'

    return prize


rest = False
game = True

while rest == False:

    print_field()

    if game == True:
        name = 'X'
        wey = int(input("Игрок № 1, ваш ход: "))
    else:
        name = 'O'
        wey = int(input("Игрок № 2, ваш ход: "))

    wey_field(wey, name)
    prize = take_line()
    if prize != '':
        rest = True
    else:
        rest = False

    game = not(game)

print_field()
print("Победил", prize)


# d = {'X': 1, '0': -1}
# arr = [['X', '0', 'X'],
#        ['X', '*', 'X'],
#        ['X', '*', 'X']]
# for i in arr:
#     for j in i:
#         if j in d:
#             print(d[j])
