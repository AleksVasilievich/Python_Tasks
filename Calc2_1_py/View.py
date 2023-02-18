from Calc import Calc


class View(Calc):
    def __init__(self):
        super().__init__()

    # @property
    def view(self):
        v = float(input())
        return v
