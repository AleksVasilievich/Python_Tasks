# Задайте натуральное число N. Напишите программу, которая составит 
# список простых делителей числа N. (1 - составное число) 

num = int(input('Введите число : '))
div = 2
col = []

while div <= num:
    if num % div == 0:
        col.append(div)
        num //= div
        div = 2
    else:
        div += 1   
print(col)         


