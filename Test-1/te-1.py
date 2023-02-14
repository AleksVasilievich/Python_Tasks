def is_prime(num):
    b = 0
    c = n
    while b != 2:
        b = 0
        c = c + 1
        for i in range(1, c + 1):
            if c % i == 0:
                b += 1
        
    return c
   

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))