def rand_weight():
    arr = [1, 2, 3, 4, 5]
    max_num = 0
    for i in arr:
        if i > max_num:
            max_num = i
    print(max_num)
    return arr  

rand_weight()      