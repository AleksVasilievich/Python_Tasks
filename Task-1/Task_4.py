# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

namber = int(input('Введите номер четверти прямоугольной системы координат -> '))
while namber < 1 or namber > 4 and namber != 0:
    namber = int(input('Введите намер четверти 1,2,3, или 4 -> '))
if namber == 1:
    print('x > 0, y > 0')
if namber == 2:
    print('x < 0, y > 0')
if namber == 3:
    print('x < 0, y < 0')
if namber == 4:
    print('x > 0, y < 0')
