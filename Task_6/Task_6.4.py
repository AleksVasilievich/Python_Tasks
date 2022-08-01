
def same_by(characteristic, objects):
    line = []
    line1 = []
    for i in objects:
        if characteristic(i) == 0:
            line.append(i)
        else:
            line1.append(i)
    if line == objects or line1 == objects:
        return True
    return False

col = [0, 2, 10, 8]
if same_by(lambda x: x % 2, col):
    print('Значения характеристики элементов одинаковы')
else:
    print('Значения характеристики элементов отличаются')
