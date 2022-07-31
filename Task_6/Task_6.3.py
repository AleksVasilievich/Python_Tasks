

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


