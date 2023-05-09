''' 
Напишите функцию solve(a, b, c), которая принимает в качестве аргументов 
три целых числа a, b, c – коэффициенты квадратного уравнения a * x * x + b * x + c = 0
и возвращает его корни в порядке возрастания.
Примечание 1. С подобной задачей мы уже сталкивались. --> (6.3-stepik)
Примечание 2. Гарантируется, что квадратное уравнение имеет корни.
Примечание. Если уравнение имеет два корня, то следует вывести их в порядке возрастания.
'''


# Вариант самый короткий №3


def solve(a, b, c):
    return min((-b - (b * b - 4 * a * c) ** 0.5) / (2 * a), (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a)), max((-b - (b * b - 4 * a * c) ** 0.5) / (2 * a), (-b + (b * b - 4 * a * c) ** 0.5) / (2 * a))


a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)

# ---------------------------------------------------------------------------
# # Вариант №1
# -----------------------------------------------------------------------------

# def solve(a, b, c):
#     d = (b * b) - (4 * a * c)
#     if d == 0:
#         return (-b / (2 * a)), (-b / (2 * a))
#     elif d > 0 and b > 0:
#         if ((-b + d ** 0.5) / (2 * a)) < ((-b - d ** 0.5) / (2 * a)):
#             return ((-b + d ** 0.5) / (2 * a)), ((-b - d ** 0.5) / (2 * a))
#         else:
#             return ((-b - d ** 0.5) / (2 * a)), ((-b + d ** 0.5) / (2 * a))
#     elif d > 0 and b < 0:
#         return ((-b - d ** 0.5) / (2 * a)), ((-b + d ** 0.5) / (2 * a))

# a, b, c = int(input()), int(input()), int(input())

# x1, x2 = solve(a, b, c)
# print(x1, x2)

# -------------------------------------------------------------------------------
# # Вариант №2 Корни должны выводится в порядке возрастания - поэтому min и max
# ------------------------------------------------------------------------------

# def solve(a, b, c):
#     d = (b * b) - (4 * a * c)
#     if d == 0:
#         return (-b / (2 * a)), (-b / (2 * a))
#     elif d > 0 and b > 0:
#         return min((-b - d ** 0.5) / (2 * a)), ((-b + d ** 0.5) / (2 * a)), max((-b - d ** 0.5) / (2 * a)), ((-b + d ** 0.5) / (2 * a))
#     elif d > 0 and b < 0:
#         return ((-b - d ** 0.5) / (2 * a)), ((-b + d ** 0.5) / (2 * a))

# a, b, c = int(input()), int(input()), int(input())

# x1, x2 = solve(a, b, c)
# print(x1, x2)


# # объявление функции
# def solve(a, b, c):
#     return min((-b-(b**2-4*a*c)**0.5)/2/a,(-b+(b**2-4*a*c)**0.5)/2/a),max((-b-(b**2-4*a*c)**0.5)/2/a,(-b+(b**2-4*a*c)**0.5)/2/a)

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)