# import itertools
#
#
# class Editor:
#     def __init__(self, data, file_name):
#         self.data = data
#         self.file_name = file_name
#
#     def generate_file(self, ):
#         f = open(self.file_name, "w")
#
#         count = 0
#
#         for s in range(10):
#             count += 1
#
#             f.write(self.data + str(count) + '\n')
#
#         f.close()
#
#     def read_file(self):
#         read_file = open(self.file_name, "r")
#         print(read_file.read())
#
#
# s = Editor("Hi there, this is line number: ", "awet.txt")
# s.generate_file()
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
