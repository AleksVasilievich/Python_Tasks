# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

col1 = [1,2,2,5,2,2,2,5,3,1,1,1,1,1,1,1]
print(col1)
col2 = []
for i in col1:
    if i not in col2:
        col2.append(i)
print(col2)        
 
# stroka = ''.join(input().split())
# print(stroka)
# new_arr = []
# for i in stroka:
#     if i not in new_arr:
#         new_arr.append(i)
# print(new_arr)
