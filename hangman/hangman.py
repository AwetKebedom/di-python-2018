

from random import randint,choice
f = open('eng.txt','r')
contenet = f.readlines()
f.close()
class HangMan:

    def __init__(self,):
        self.words = choice(contenet)

    def play(self):
        self.life_of_player = len(self.word)+5
        self.word = self.choose_word()
        self.encrypted = self.encrypted_word()

        used_letters = ''

        while True:
            userletter = input("choose any letter\n")

            if userletter in used_letters:
                print("Letter already used")
            else:
                used_letters += userletter
                break
        self.encrypted_word = self.decrypted_word()

        userletter = input("choose letter")

        for letter in range(len(self.word)):
            if userletter in self.word[letter]:
                self.encrypted_word = self.decrypted_word()
            else:
                self.life_of_player -= 1










    def help(self):
        pass

    def choose_word(self):
        word = words[randint(0,len(words)-1)]
        word = list(word)
        return word

    def encrypted_word(lsef, word):

        return "*"* len(word)

    def decrypted_word(self,letter):

        new_word = ''
        for charachter in range(len(self.encrypted)):
            if letter in self.word[charachter]:
                new_word += letter
            else:
                new_word += self.encrypted[charachter]
        return new_word














