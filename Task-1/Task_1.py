# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:  - 6 -> да ; - 7 -> да  ; - 1 -> нет.

namber = int(input('Введите номер дня недели ->  '))
while namber < 1 or namber > 7:
   namber = int(input('Введите число от 1 до 7 ->  ')) 
if namber == 1 or namber == 2 or namber == 3 or namber == 4 or namber == 5:
    print('No')
elif namber == 6 or namber == 7:
    print('Yes')

