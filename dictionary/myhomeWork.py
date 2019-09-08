myList = []
while True:
    usernumber = input("please type any number: \n")
    if usernumber == 'stop':
        break
    usernumber = int(usernumber)
    if usernumber not in myList:
        myList.append(usernumber)
    maxi = myList[0]
    mini = myList[0]
    for number in myList:
        if number > maxi:
            maxi = number
        elif number < mini:
            mini = number
print("myList : >>", myList)
print("maximum number is", maxi)
print("and the minimum number is ", mini)
