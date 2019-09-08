import json

# with open('shoes.json', 'r') as f:
#     file = json.load(f)
# shoes = file["shoes"]

# counting_shoes = {}
# for s in shoes:
#     if s["brand"] in counting_shoes.keys():
#         counting_shoes[s["brand"]] += 1
#     else:
#         counting_shoes[s['brand']] = 1
#
# print(counting_shoes)


# customer = input("what do you want to buy?")

# fount_it = False

# for shoe in shoes:
#     if customer.upper() == shoe['brand'].upper() or customer.upper() == shoe["name"]:
#         fount_it = True
#         print("we have this shoe : {}, from this brand: {}, and the price is: {}".format(shoe["name"], shoe["brand"],
#                                                                                          shoe["price"]))
# if not fount_it:
#     print("sorry we dont have this")

with open("tematos.json","r") as f:
    products = json.load(f)

class Basket:
    def __init__(self,name):
        self.name = name
        self.basket = {}
        self.total = 0

    def ask_user(self):
        user_query = input("Hi {}, how are you today?\n what can I help you?\n>>>")
        while True:
            if user_query in products.keys():
                number_items = int(input('how many items ?'))
                self.basket[user_query] = number_items
            else:
                print('we do not have this item')
            other_query = input('do you want something else\n')
            if other_query == 'yes':
                user_query = input('what else do you want \n')
            else:
                break

    def calculate_total(self):
        for item in self.basket.keys():
             self.total += self.basket[item] * products[item]['price']
        print('this is the amount you need to pay: {}$'.format(self.total))


customer_name = input('what is your name')

customer_basket = Basket(name=customer_name)

customer_basket.ask_user()

customer_basket.calculate_total()






