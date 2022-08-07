

poem = input()
# poem = 'Пара-ра-рам рам-пам-папам па-ра-па-дам'
print(poem)
vowels = 'аеёиоуыэюя'
space = ' '
count = 0
count1 = 0
for i in poem:
    if i in space:
        count1 = count
        count = 0
    else:
        if i in vowels:
            count += 1
if count != count1:
    print('Пам парам')
else:
    print('Парам пам пам')

# print(count1)
# print(count)


# Винипух от Дениса
#
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
