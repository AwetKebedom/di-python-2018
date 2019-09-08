# Exercise 1


# def add_num_to_file(filename,num):
#
#     for nb in range(num+1):
#
#         file = open(filename,'a')
#         file.write(str(nb) + '\n')
#         file.close()
#
# add_num_to_file('file1.txt',10)




# Exercise 2


# def copy_file(filename,filename2):
#     file = open(filename, 'r')
#     content  = file.read()
#     file.close()
#     file2 = open(filename2, 'w')
#     file2.write(content)
#     file2.close()
#     print(content)
#
#     file2.close()
# copy_file('file1.txt','copy-file.txt')


# Exercise 3

# file = open('file1.txt', 'r')
# lines = file.readlines()
# file.close()
# file2 = open('reversed.txt', 'w')
# for line in range(len(lines) - 1, -1, -1):
#     for chart in range(len(lines[line]) - 1, -1, -1):
#         file2.write(lines[line][chart])
# file2.close()




#  Exercise 4

# def concatnate(file_lists, filename):
#     doc2 = open(filename, 'w')
#
#     for file in file_lists:
#         doc = open(file, 'r')
#         content = doc.read()
#         doc2.write(content)
#         doc.close()
#
#     doc2.close()
#
# concatnate(['file1.txt','file2.txt','file3.txt'],'main.txt')


# Exercise 5

# def split_extension(filename):
#
#     file = open(filename, 'r')
#     name = file.name
#     print(name.split('.'))
#
# split_extension("file2.txt")




