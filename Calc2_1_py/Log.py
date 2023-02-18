from Output import Output


class Log:
    def log(self):
        data_calc2 = []
        data = ""

        data_calc2.append(Output.out(str(self)))

        data = ''.join(str(*data_calc2))

        print(data)

        with open('Calc2_1_py\calc2_1.txt', 'a', encoding='utf_8') as file:
            file.write(data)
