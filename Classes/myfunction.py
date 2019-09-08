# def checking_inputs():
#     user = input("please type any word")
#
#     alphabet ="abcdefghijklmnopqrstuvwxyz"
#     for letter in user:
#         if letter in alphabet:
#             return True
#         return False

def Validate_password():
    password = input('Enter your password')
    password_letters = list(password)
    upper = False
    lower = False


    for letter in password_letters:
        if letter.isupper():
            upper = True
        elif letter.islower():
            lower = True

        if upper and lower:
            print("valid")
            return True
        print("invalid")
        return False




# if len(password) <= 5:
#     print('password is to short')
# elif name.lower() in password.lower() or surname.lower() in password.lower():
#     print('You cannot have first or last name in password')
# elif not (upper and lower):
#     print('You must have both upper and lower case in password')
# else:
# print('Password is valid')




