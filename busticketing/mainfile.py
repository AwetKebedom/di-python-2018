#
# def sort_list(my_list):
#     sorted_list = []
#     minimum = my_list[0]
#
#     for x in range(len(my_list)):
#
#         for i in my_list:
#
#             if i <= minimum:
#                 minimum = i
#
#     sorted_list.append(minimum)
#     my_list.remove(i)
#
#
#     return sorted_list
# print(sort_list([1,5,4,8,7,9]))
#
#
# def question_answer(question, answer):
#     print(question)
#     user = input(">>>")
#     if user == answer:
#         print("yes it is")
#         return True
#
#     print("No, you are wrong it is {}".format(answer))
#     return False
# print(question_answer("what is the capital of Israel\n","Jerusalem"))
#
# def question_and_answer(string):
#     splited_string = string.split('::')
#     #print("The question is \t {} \nAnd the answer is \t {}".format(splited_string[0], splited_string[1]))
#     my_dict = {"question": splited_string[0],
#                "answer": splited_string[1]}
#     return my_dict
#
#
# print(question_and_answer("How old are you Awet?::36"))
# def ask_question(string):
#     my_dict = question_and_answer(string)
#     return question_answer(my_dict['question'], my_dict['answer'])
#
# print(ask_question("who is the prime  minister::Bibi"))
#
#
# def asking_multiple_questions(list_of_questions):
#
#     for question in list_of_questions:
#         x = ask_question(question)
#
#     return True
# print(asking_multiple_questions(["How old is Awet?::36","How old is Rueven?::40","What is the best language in the world?::Python"]))
letters = ['a','s','d','e']
words = 'awetkebedom'
g = 's'
for m in range(len(letters)):
    if letters[m]==g:
        letters[m] = "m"
print(letters)