# class Dog:
#     def __init__(self, color, type, age):
#         self.color = color
#         self.type = type
#         self.age = age
#         self.energy = 100
#         self.energy_per_km = 20
#
#     def my_function(self):
#         print("This Dog has {} color and from {} type".format(self.color, self.type))
#
#     def birth_day(self):
#         if self.age > 15:
#             print("your dog has died")
#         else:
#             print("your dog is alive")
#             self.age += 1
#
#     def walk(self):
#
#         if self.energy <= 0:
#             return False
#         else:
#             print("your dog can travel {} kms".format(self.energy))
#             self.energy -= 20
#
#     def rest(self):
#         self.energy = 100
#         print("your dog has energized")
#
#     def checking(self,kilo_to_travel):
#         required_energy = self.energy_per_km*kilo_to_travel
#         if required_energy <= self.energy:
#             return False
#         return True
#
#
#
#
#
#
#
# dog1 = Dog('black and white', "boofon", 24)
# dog2 = Dog("white", "tarzan", 12)
# # for _ in range(5):
# #     dog2.birth_day()
# # for _ in range(6):
# #     dog1.walk()
# enough_energy = dog1.checking(5)
# if enough_energy == False:
#     dog1.rest()
#
#
#
#
#

# class Airport:
#     def __init__(self, capacity, name):
#         self.capacity = capacity
#         self.name = name
#         self.current_planes = 0
#
#     def plane_in(self,current_planes):
#         if self.current_planes <= self.capacity:
#             self.current_planes += 1 # enough place for everyone
#             return True
#         self.capacity = self.current_planes
#         # not enough place for everyone
#
#         return False
#
#
#     def plane_out(self):
#         if self.current_planes >0:
#             self.current_planes -= 1
#             return False
#
# my_airport = Airport(20, "Bengurion")
# my_second_airport = Airport(50, "Asmara")
# print(my_airport.current_planes)
# print(my_airport.plane_in(20))
# print(my_airport.current_planes)
#

class restaurant:
    def __init__(self, nb_tables, current_clients, opening_hours, closing_hours):
        self.capacity = 5
        self.nb_tables = nb_tables
        self.current_clients = current_clients
        self.opening_hours = opening_hours
        self.closing_hours = closing_hours

    def client_in(self, hour):
        if self.check_opening(hour) == False:
            print("sorry it is closed!")
            return False
        table = self.check_table()
        if table == False:
            print("sorry we don't have table.")
            return False
        self.current_clients[table] = True
        return "you are welcome"

    def check_opening(self, hour):
        if self.opening_hours < hour < self.closing_hours:
            return True
        return False

    def check_table(self):
        for key in self.current_clients.keys():
            if self.current_clients[key] == False:
                return key
        return False

resturant1 = restaurant(5,{0:True,
                           1:True,
                           2:False,
                           3:False,
                           4:True},8,18)
print(resturant1.client_in(5))




#print(resturant1.check_table())


# class user:
#     def __init__(self, name, email, password):  # creating an object constructor;
#         self.name = name
#         self.email = email
#         self.password = password
#         self.logged_in = True
#         self.msg_box = []
#
#     def log_in(self):
#         user_name = input('please write user name')
#         user_password = input("password:")
#
#         if self.name == user_name and self.password == user_password:
#             print("you are logged in")
#             self.logged_in = True
#         else:
#             print("Please check your entries")
#
#     def change_password(self):
#         new_password = input('type new password')
#         self.password = new_password
#
#     def send_message(self, person_to_send, msg):
#         self.msg_box.append(msg)
#
#
# person1 = user("awet", "awetk@gmail.com", "12354")
# person2 = user("eyal", "eyal@gmail.com", "68787")
# person1.change_password()
# person1.log_in()
# person1.send_message(person2, "hello, how are you doing my dear")
# print(person1.msg_box)
