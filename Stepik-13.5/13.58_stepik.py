'''
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента 
непустую строку text, состоящую из символов ( и ) и возвращает значение True 
если поступившая на вход строка является правильной скобочной последовательностью 
и False в противном случае.
Примечание 1. Правильной скобочной последовательностью называется строка, 
состоящая только из символов ( и ), где каждой открывающей скобке найдется 
парная закрывающая скобка (при этом каждая открывающая скобка должна быть 
левее соответствующей ей закрывающей скобки).
'''

def wrong_character(text):
    count = 0
    for i in text:
        if i != "(" and i != ")":
            count += 1

    return count == 0
        

def even_left_and_right(text):
    
    left_text = 0
    right_text = 0
    
    for i in text:
        if i == '(':
            left_text = left_text + 1
        else:
            right_text = right_text + 1
            if left_text < right_text:
                return False
                break
            
    return left_text - right_text == 0


def is_correct_bracket(text):
    flag = wrong_character(text) and even_left_and_right(text)

    return flag

txt = "()()()"

print(is_correct_bracket(txt))