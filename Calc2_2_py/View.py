from Calc import Calc


class View(Calc):
    def __init__(self):
        super().__init__()

    def view(self, prompt=""):
        if prompt:
            print(prompt)
        return float(input())