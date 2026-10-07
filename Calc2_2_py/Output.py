from View import View
from Model import Model
from Log import Log


class Output:
    @staticmethod
    def out():
        view = View()
        model = Model()

        v = int(input("Введите команду (1-4): "))
        a = view.view("Введите первое число:")
        b = view.view("Введите второе число:")

        try:
            result = model.result(v, a, b)
        except ValueError as e:
            print(e)
            return None

        Log.log(result)
        return result