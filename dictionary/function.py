# def make_shirt(size, text):
#     print('You chose a shirt with {} size and {}message in it'.format(size, text))
#
# make_shirt('M', ' I LOVE YOU ')
#
# def make_shirt(text, size = 'large'):
#     print('You chose a shirt with {} size and {}message in it'.format(size, text))
#
# # make_shirt('I LOVE PYTHON ')
#
# def check(a, b):
#
#     if type(a) == int and type(b) == int:
#
#         print(a + b)
#     else:
#         print('they are no numbers')
#
# check('kl', 6)

# def traingle(m):
#     for s in range(m):
#         print('*'*s)
#
# traingle(6)

# def traingle(m):
#     for s in range(m):
#         print('* '*s)
#     for s in range(m):
#         print('* '*(m-s))
#
#
#
#
#
# traingle(6)

# Excerise 1.

# myList = [7,9,8,11,10,0,1]
# max = myList[0]
# for n in myList:
#     if n > max:
#         max = n
# print(max)

# Exercise 2.

# myList = [7,9,8,11,10,0,1]
# second = myList[:]
# print(second)

# OR
# myList = [7,9,8,11,10,0,1]
# second = []
# for a in myList:
#     second.append(a)
# print(second)

# Excercise 3.


# my_list = ["I", "is", "a", "list"]
# for n in range(len(my_list)):
#
#     print(n,'\t:', my_list[n])

# Functions

# Exercise 1.

# def myFunc(a, b):
#     count = 0
#     for n in a:
#         if n == b:
#             count += 1
#     return (b, 'apears ', count, 'times')
#
#
# print(myFunc([1, 2, 0,3, 8, 5, 5],8))

# Exercise 2

# my_list= ['this', 'is', 'a', 'string']
# i = 0
# mystring = ''
# while i < len(my_list):
#     mystring += (my_list[i] + ' ')
#     i +=1
# print(str(mystring))

# def myFunc(myList):
#     i = 0
#     mystring = ""
#     while i < len(myList):
#         mystring += (myList[i] + ' ')
#         i += 1
#
#     return mystring
#
# print(myFunc(['this', 'is', 'a', 'string']))

#Exercise 3
#
# def check(capital):
#     if capital == capital.upper():
#         return True
#     return False
#
#
# print(check('this is a string'))

# def checking(my_string):
#     ucase = 0
#     lcase = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for letter in my_string:
#         if letter.lower() in alphabet:
#             if letter == letter.upper():
#                 ucase += 1
#             else:
#                 lcase += 1
#     return ucase,lcase
# print(checking("this Is My My Dream."))



















# def myList(num):
#     new_list = []
#     for m in range(num):
#         new_list.append(m)
#     return new_list
# print(myList(6))

# def myList(num):
#     new_list = []
#     i = 0
#     while i < num:
#         new_list.append(i)
#         i += 1
#     return new_list
# print(myList(6))

# def myList(num, ):
#     new_list = []
#     for s in range(num):
#         new_list.append(s)
#     return new_list
# print(myList(4))
#






















