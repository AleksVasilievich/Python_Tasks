# Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования.

# В рамках этого обсуждения студентам надо нарисовать “архитектуру” (например, в виде блок-схемы)
# для работы данного приложения.






# import controller as c

# c.button_click()
# main




# # import model_mult as model      # Для умножения
# # import model_sum as model       # Для сложения
# import model_sub as model       # Для вычитания

# import view

# def button_click():
# def view_data(data, title):
#     print(f'{title} = {data}')


# x=0
# y=0

# def init(a, b):
#     global x
#     global y
#     x=a


#     y=b

# def do_it():
# 	return x*y



# values = [3, 6, 9, 12, 15]
# transformed_values = list(map(lambda x: x, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# планета
# def find_farthest_orbit(arr):
#     return [i for i in arr if i[0] * i[1] == max([i[0] * i[1] for i in arr if i[0] != i[1]])]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Винипух
# def check(text):
#     sets = set()
#     for i in text.split():
#         count = 0
#         for j in i:
#             if j in 'ауоыиэяюёе':
#                 count += 1
#         sets.add(count)
#     if len(sets) == 1:
#         return 'yes'
#     return 'no'


# text = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# print(check(text))


# таблица
# def print_operation_table(operation, rows=9, columns=9):
#     for i in range(1, rows + 1):
#         for j in range(1, columns + 1):
#             if i > 1 and j > 1:
#                 print(operation(i, j), end='\t')
#             else:
#                 print(i * j, end='\t')
#         print()

# def print_operation_table(operation, rows=9, columns=9):
#     for i in range(1, rows + 1):
#         for j in range(1, columns + 1):
#             if i > 1 and j > 1:
#                 print(operation(i, j), end='\t')
#             else:
#                 print(i * j, end='\t')
#         print()


