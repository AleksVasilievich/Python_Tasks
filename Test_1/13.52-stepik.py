''' 
Напишите функцию is_prime(num), которая принимает в качестве аргумента 
натуральное число и возвращает значение True если число является простым 
и False в противном случае.
'''

def is_prime(num):
    b = 0
    for i in range(1, n + 1):
        if n % i == 0:
            b = b + 1
    if b == 2:
        return True
    else:
        return False
            

n = int(input())

print(is_prime(n))


# def is_prime(num):
#     return len([i for i in range(1, num+1) if num % i == 0]) == 2

# n = int(input())    
# print(is_prime(n))