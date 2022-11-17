def imp_f():
    path = 'Task_1/Task_16.1/data_1.txt'
    data = open(path, 'r', encoding='utf_8')
    for line in data:
        print(line)
    data.close()