def is_prime(num):
    # flag = False
    b = 0
    for i in range(1, n + 1):
        if n % i == 0:
            b = b + 1
    return b == 2
    # if b == 2:
    #     flag = True
    # return flag   
    # return len([i for i in range(1, num+1) if num % i == 0]) == 2       

n = int(input())
print(is_prime(n))