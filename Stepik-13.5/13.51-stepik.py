''' 
Напишите функцию is_valid_triangle(side1, side2, side3), 
которая принимает в качестве аргументов три натуральных числа, 
и возвращает значение True если существует невырожденный треугольник 
со сторонами side1, side2, side3 и False в противном случае.
Примечание 1. С данной задачей мы уже сталкивались 
при изучении условного оператора.
'''

def is_valid_triangle(side1, side2, side3):
    if (a + b) > c and (a + c) > b and (c + b) > a:
        return True
    else:
        return False
        

a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))