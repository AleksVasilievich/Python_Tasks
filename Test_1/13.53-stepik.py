'''
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента 
натуральное число num и возвращает первое простое число большее числа num.
Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
'''

def is_prime(num):
    b = 0
    for i in range(1, num + 1):
        if num % i == 0:
            b = b + 1
    return b == 2

def get_next_prime(num):
    c = n + 1
    while is_prime(c) == False:
        c = c + 1
    return c

n = int(input())
print(get_next_prime(n))


# Вариат №2 без использования внутринней функции для проверки на простоту числа

# def get_next_prime(num):
#     b = 0
#     c = n
#     while b != 2:
#         b = 0
#         c = c + 1
#         for i in range(1, c + 1):
#             if c % i == 0:
#                 b += 1
        
#     return c
   

# n = int(input())

# print(get_next_prime(n))