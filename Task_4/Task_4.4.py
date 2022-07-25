# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и вывести на экран.
# Пример:    - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

k = int(input("Введите положительное целое число - степень многочлена ->  "))
col = [random.randint(0, 101) for i in range(k + 1)] 
col = col[::-1]  
func = '' 
for i in range(len(col)):
    if i != len(col) -1 and i != len(col) -2 and col[i] != 0:
        func += f'{col[i]}x^{len(col)-i-1}'
        if col[i + 1] != 0:
            func += ' + '
    elif i == len(col) - 2 and col[i] != 0:
        func += f'{col[i]}x'
        if col[i + 1] != 0:
            func += ' + '    
    elif i == len(col) - 1 and col[i] != 0:
        func += f'{col[i]} = 0'
    elif i == len(col) - 1 and col[i] == 0:
        func += ' = 0'

print(func)
