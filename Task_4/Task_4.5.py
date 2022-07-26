# 35(Доп). Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt','w',encoding='utf-8') as data1:
    data1.writelines('1,3,5,7')
   

with open('file2.txt','w',encoding='utf-8') as data2:
    data2.writelines('2,4,6,8')
   
num1 = open(r'C:\Users\Александр\Desktop\GeekBrains\PYTHON_BLOCK\Python Tasks\file1.txt','r')
nam1 = num1.read() + ''
num1.close()

print(nam1)
   
num2 = open(r'C:\Users\Александр\Desktop\GeekBrains\PYTHON_BLOCK\Python Tasks\file2.txt','r')
nam2 = num2.read() + ''
num1.close()

print(nam2)