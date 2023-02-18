from Calc import Calc

class Model(Calc):
    def __init__(self):
        super().__init__()

    def result(self, z, x, y):

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
        return exit("Неверный ромер команды")
