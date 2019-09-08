user_1_name = input("Hi first user, What is your name  \n")
user_1 = int(input( user_1_name+", what is your height?\n"))
user_2_name = input("Hi second user, What is your name  \n")
user_2 = int(input( user_2_name+", what is your height?\n"))
if user_1 > user_2 and user_1!=user_2:
    print( user_1_name, "you are taller than", user_2_name)
elif user_1 == user_2:
    print(" your heights are the same ")
else:
    print( user_2_name, ",you are taller than " + user_1_name)