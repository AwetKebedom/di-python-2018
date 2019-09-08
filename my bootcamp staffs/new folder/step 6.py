
user = input('Please type here any of your favorite fruits: \n')
new_one = user.split(' ')
i = 0
while i < len(user):
    choice = input('Please type here any  fruits: \n')
    while i < len(new_one):
        if new_one[i] != choice:
            continue
        else:
            print('yes')
        i += 1
    i += 1





