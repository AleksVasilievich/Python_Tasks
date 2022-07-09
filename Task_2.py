# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

amount = 3
option = 2
result = option ** amount
sum = 0
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if not (x + y + z) == (not x) * (not y) * (not z):
                sum += 1
if result == sum:
    print('Истина')
else:
    print('Лож')
