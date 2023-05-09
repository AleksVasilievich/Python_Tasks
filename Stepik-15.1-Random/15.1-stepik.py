# Модуль random

#   Модуль random предоставляет функции для генерации 
# случайных чисел, букв и случайного выбора элементов 
# последовательности (списка, строки и т.д.).

# ---------------------

# Функция randint()  принимает два обязательных аргумента a и b 
# и возвращает случайное целое число из отрезка [a;b].

import random

num1 = random.randint(0, 17)
num2 = random.randint(-5, 5)

print(num1)
print(num2)

print('----------------------------')

random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100))

print('----------------------------')

# Функция randrange() возвращает случайно выбранное число из последовательности чисел.

num = random.randrange(10)
print(num)

num = random.randrange(5, 10)
print(num)

num = random.randrange(0, 101, 10)
print(num)

print('----------------------------')

# Функция random()  возвращает случайное число с плавающей точкой (вещественное число).

num = random.random()
print(num)

#----------------------------------------

''' 
random.uniform(a, b)                          

Возвращает псевдослучайное число с плавающей   запятой в      диапазоне от a до b.               
random.randint(a, b)                          

Возвращает псевдослучайное целое число в диапазоне от a до b.
random.choice(a)                            

Возвращает псевдослучайный элемент из любой последовательности.
random.randrange(a, b, c)                     

Возвращает псевдослучайное число из диапазона от a до b с шагом c.
random.shuffle(a)                 

Перемешивает последовательность.
random.sample(population, k)                  

Возвращает список длиной k из уникальных элементов, выбранных из последовательности или множества.
'''

#Примечание 2. Функции модуля random на самом деле являются методами одноименного класса random.

#Примечание 3. Функция randint() реализована на основе функции randrange() следующим образом:

# Return random integer in range [a, b], including both end points.
def randint(self, a, b):
    return self.randrange(a, b + 1)

print('-------------------------')

# Задача.

for _ in range(10):
    numl = random.randint(0, 1)
    if numl == 0:
        print('Орел')
    else:
        print('Решка')

print('-------------------------')

[print(('Решка', 'Орел')[__import__('random').randint(0, 1)]) for _ in range(5)]

print('-------------------------')

numlm = random.randint(1, 118)
print(numlm)
