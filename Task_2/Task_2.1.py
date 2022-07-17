# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.   # Пример:         6782 -> 23      0,56 -> 11


num = input('Введите вещественное число  -> ')

num1 = int(num)
sum1 = 0
while num1 > 0:
    sum1 += num1 % 10
    num1 //= 10
print(sum1)
 
num = str(num)
num2 = int(num.split('.')[1])
print(num2)

sum2 = 0
while num2 > 0:
    sum2 += num2 % 10
    num2 //= 10
print(sum2)
print(sum1 + sum2)
 
