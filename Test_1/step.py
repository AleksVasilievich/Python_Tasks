# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     elif password.islower() or password.isdigit() or password.isalpha() or password.isupper():
#         return False
#     else:
#         return True

# txt = input()

# print(is_password_good(txt))


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
