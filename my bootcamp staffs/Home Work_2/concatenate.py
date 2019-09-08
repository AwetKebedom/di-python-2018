min = max = userInput = input( " Enter any number: ")
while userInput != "stop":
    if int(userInput) < int(min):
        min = int(userInput)
    elif int(userInput) > int(max):
        max = int(userInput)
    userInput = input( "Enter any number: ")
print ("Min is "+str(min))
print ("Max is "+str(max))