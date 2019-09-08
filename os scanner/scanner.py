# # import os
# #
# #
# # # print(list(os.scandir()))
# # # print(os.listdir())
# # content = os.scandir()
# # for a in content:
# #     try:
# #         file = open(a.name, 'r')
# #
# #     except:
# #         pass
# #     else:
# #         print(file.read())
# #         file.close()
# #
#
# import time
# # print(2**38)
# # def return_decrypted_letter(letter):
# #     alphabet = 'abcdefghijklmnopoqrstuvwxyz'
# #     if letter not in alphabet:
# #         pass
# #     else:
# #         lx = alphabet.index(letter.lower())
# #         new_index = lx + 2
# #         new_letter = alphabet[new_index]
# #     return new_letter
# #
# # def conver_word(word):
# #     new_word = ''
# #     for letter in word:
# #
# #         new_word +=return_decrypted_letter(letter)
# #     return new_word
# #
# # conver_word("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
# #
# # def return_decrypted_letter(letter):
# #     alphabet = 'abcdefghijklmnopoqrstuvwxyz'
# #
# #     if letter not in alphabet:
# #         letter = ''
# #
# #
# #     lx = alphabet.index(letter.lower())
# #     new_index = lx + 2
# #     if new_index > 26:
# #         new_index -=26
# #     new_letter = alphabet[new_index]
# #     return new_letter
# #
# #
# # def return_decrypted_word(word):
# #     new_word = ''
# #
# #
# #     for leters in word:
# #         new_word += return_decrypted_letter(leters)
# #     return new_word
# # print(return_decrypted_word("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))
# #
#
# def new_word(string):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     new_word = ''
#
#
#     for letter in string:
#         if letter not in alphabet:
#             new_word += letter
#             continue
#
#         lx = alphabet.index(letter)
#         lx2 = lx + 2
#         if lx2 >= 26:
#             lx2 -= 26
#
#
#
#         new_letter = alphabet[lx2]
#
#         new_word += new_letter
#
#     print(new_word)
#
#
#
#
#
#
#
#
# new_word("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")


