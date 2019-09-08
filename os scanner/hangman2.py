from random import choice

f = open('eng.txt','r')
content = f.readlines()
f.close()


class Hangman:
    def __init__(self):
        self.word =choice(content)


        self.encrypted_word = " _ " * len(self.word)
        self.max_life = 10

    def play_game(self):
        print("Hello and welcome to Hangman game:")
        print(self.encrypted_word)

        used_letter = []
        correct_letter = []

        while True:

            print("\n")

            while True:
                user_letter = input("Please guess any letter:\n >>>")

                if user_letter in used_letter:
                    print("Letter already guessed once. Please Try other.")
                else:
                    break

            success_flag = True
            for character in self.word:
                if character == user_letter or character in correct_letter:
                    print(character, end = ' ')
                    used_letter.append(user_letter)





                    correct_letter.append(user_letter)

                else:
                    print(" _ ", end=' ')
                    used_letter.append(user_letter)
                    success_flag = False
                    self.max_life -=1

            if success_flag:
                print("You won")
                break


n = Hangman()
n.play_game()