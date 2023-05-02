''' 
Напишите функцию is_password_good(password), которая принимает в качестве аргумента 
строковое значение пароля password и возвращает значение True 
если пароль является надежным и False в противном случае.
Пароль является надежным если:
его длина не менее 8 символов; 
он содержит как минимум одну заглавную букву (верхний регистр); 
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
'''

def is_password_good(password):

    if len(password) < 8 :
        return False

    if not password.isalnum():
        return False   
    
    if password.isupper():
        return False   

    if password.islower():
        return False

    if password.isdigit():
        return False

    if password.isalpha():
        return False

    return True
    

     
txt = input()
print(is_password_good(txt))
