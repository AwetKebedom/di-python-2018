# class BusTicketSystem:
#     def __init__(self):
#         self.nb_of_seats = 10
#         self.booked_seat = [False, False, False, False, False, False, False, False, False, False]
#         self.cost_per_ticket = 50
#
#     def main(self):
#         self.show_menu()
#
#     def show_menu(self):
#
#         print("here are the options to select, if you want to exit, please type 'x' to exit ")
#
#         print("(a)--book a seat\n",
#               "(b)--pay for a ticket\n",
#               "(c)--view information about the bus\n",
#               "(x)--exit\n")
#
#         while True:
#             user_input = input("please select an option from the above lists\n>>> ")
#             if user_input == 'x':
#                 return False
#             elif user_input == "a":
#                 return self.book_seat(2)
#             elif user_input == "b":
#                 return self.pay_for_ticket()
#             elif user_input == "c":
#                 return self.show_bus_info()
#             else:
#                 print("error")
#
#     def book_seat(self, seats):
#         user_input = input('Please confirm you want to book a seat on the bus.[Y/n]')
#         if user_input == 'n':
#             return False
#         elif user_input == 'y':
#             free_seat = 0
#
#
#
#             if False not in self.booked_seat:
#                 print("sorry we don't have enough seats")
#                 return False
#             else:
#                 for seat in range(len(self.booked_seat)):
#                     if self.booked_seat[seat] == False:
#                         free_seat += 1
#                         self.booked_seat[seat] = True
#                     if free_seat >= seats:
#                         free_seat -= seats
#
#                         return free_seat
#
#                     return False
#
#     def calculate_cost(self,seat):
#         total_cost = seat*self.cost_per_ticket
#         return total_cost
#
#     def pay_for_ticket(self):
#         print('our service costs 50 shekles for a seat and we accepts only bank notes not coins of 20 50 100 and 200')
#         bank_note = int(input("please type your bank notes here; /n"))
#
#         if bank_note % 20 !=0 or bank_note % 50 !=0 or bank_note % 50 !=0  or bank_note % 100 !=0 or bank_note % 200 !=0:
#             print(" you tried to pay with unacceptable currency")
#         else:
#             if self.calculate_cost() < bank_note:
#                 change = bank_note - self.calculate_cost()
#
#             print(change , " is your change and thank you for visiting our site.")
#
#     def free_table(self):
#         free_seat = 0
#         for seat in range(len(self.booked_seat)):
#             if self.booked_seat[seat] == False:
#                 free_seat += 1
#         return free_seat
#
#
#
#
#     def show_bus_info(self):
#
#         print(" welcome to our service site and we are pleased to serve you prudently.")
#         print("we have maximum of 10 seats in this bus")
#         print("we have {} seats to be booked ".format(self.free_table()))
#
#
# bus1 = BusTicketSystem()
# bus1.main()
#


class Airport:

    def __init__(self, name, capacity):
        # Arguments attributes
        self.name = name
        self.capacity = capacity

        # Default attributes
        self.current_planes_nb = 0

    def plane_in(self, n=1):
        if (self.current_planes_nb + n) < self.capacity:
            self.current_planes_nb += n
            return True
        return False

    def plane_out(self, n=1):
        if (self.current_planes_nb - n) >= 0:
            self.current_planes_nb -= n
            return True

        return False

    def describe(self):
        print("Airport {}: {}/{} planes".format(self.name,
                                                self.current_planes_nb,
                                                self.capacity))

    def ui(self):

        print("Hey, welcome to {} Airport".format(self.name))

        while True:
            print("\n\n")
            print("What do you want to do? (Choose a number)")
            print("0) Exit")
            print("1) Add planes")
            print("2) Remove planes")
            print("3) Get airport status")

            choice = input(">>> ")
            if choice not in ["0", "1", "2", "3"]:
                print("Please enter 0, 1 or 2")
                continue

            if choice == "0":
                print("Goodbye!")
                break

            elif choice == "1":  # PLANE IN
                nb_of_planes = input("How many planes do you wanna add?\n>>> ")
                try:
                    nb_of_planes = int(nb_of_planes)
                except:
                    print("wrong number of planes")
                    continue

                if self.plane_in(nb_of_planes):
                    print("{} planes entered {}".format(nb_of_planes, self.name))
                else:
                    print("Sorry, no more places available")

            elif choice == "2":  # PLANE OUT
                nb_of_planes = input("How many planes do you wanna remove?\n>>> ")
                try:
                    nb_of_planes = int(nb_of_planes)
                except:
                    print("wrong number of planes")
                    continue

                if self.plane_out(nb_of_planes):
                    print("{} planes left from {}".format(nb_of_planes, self.name))
                else:
                    print("You have no planes in your airport")

            elif choice == "3":
                self.describe()


myairport = Airport(capacity=10, name="Ben Gurion")
myairport.ui()