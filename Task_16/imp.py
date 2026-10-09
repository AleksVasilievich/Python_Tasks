def imp_f():
    path = 'data.txt'
    data = open(path, 'r', encoding='utf_8')
    for line in data:
        print(line)
    data.close()