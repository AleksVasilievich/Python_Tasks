import input_calc as inp
import out_calc as out
import mod_calc as c


def exp_calc2():

    data_calc2 = []
    data = ""
    
    data_calc2.append(out.view_res())
    
    print(data_calc2)

    data = ''.join(str(data_calc2))

    print(data)


    with open('Test-2\calc2.txt', 'a', encoding='utf_8') as file:
        file.write(data)

