import mod_calc as c
import input_calc as inp

def view_res():

    a = inp.print_calc()
    b = inp.print_calc()
    v = inp.print_calc()

    # print(c.result(a, b, v))
    return c.result(a, b, v)