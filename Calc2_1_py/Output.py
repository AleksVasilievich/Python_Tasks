from Model import Model
from View import View


class Output:
    def out(self):
        a = View.view(self)
        b = View.view(self)
        v = View.view(self)
        return Model.result(self, a, b, v)  
