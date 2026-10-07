from Calc import Calc


class Model(Calc):
    def __init__(self):
        super().__init__()

    def result(self, z, x, y):
        if z == 1:
            return f"{x} + {y} = {x + y}"
        if z == 2:
            return f"{x} - {y} = {x - y}"
        if z == 3:
            return f"{x} * {y} = {x * y}"
        if z == 4:
            return f"{x} / {y} = {x / y}"
        raise ValueError("Неверный номер команды")