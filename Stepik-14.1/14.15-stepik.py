''' 
Напишите функцию get_month(language, number), которая принимает 
на вход два аргумента language – язык ru или en 
и number – номер месяца (от 1 до 12) и возвращает название месяца 
на русском или английском языке.
'''

def get_month(language, number):
    li_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 
            'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

    li_en = ['january', 'february', 'march', 'april', 'may', 'june', 
            'july', 'august', 'september', 'october', 'november', 'december']
    
    if lan == 'ru':
        return li_ru[num - 1]
    elif lan == 'en':
        return li_en[num - 1]

lan = input()
num = int(input())

print(get_month(lan, num))