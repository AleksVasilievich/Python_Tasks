

def result(z, x, y):

    # c = int(input())

    if z == 1:
        res_st = str(x) + ' + ' + str(y) + ' = ' + str(x + y) + '\n'
        return res_st
    if z == 2:
        res_st = str(x) + ' - ' + str(y) + ' = ' + str(x - y) + '\n'
        return res_st
    if z == 3:
        res_st = str(x) + ' * ' + str(y) + ' = ' + str(x * y) + '\n'
        return res_st
    if z == 4:
        res_st = str(x) + ' / ' + str(y) + ' = ' + str(x / y) + '\n'
        return res_st        

