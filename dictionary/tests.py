# class Airport:
#
#     def __init__(self, name, capacity):
#         # Arguments attributes
#         self.name = name
#         self.capacity = capacity
#
#         # Default attributes
#         self.current_planes_nb = len(self.airplanes)
#         self.airplanes = [Plane.plane_map[i] for i in Plane.plane_map]
#
#     def plane_in(self, plane):
#         if (self.current_planes_nb ) < self.capacity:
#
#             self.current_planes_nb += 1
#             self.airplanes.append(plane)
#             return True
#         else:
#             return False
#
#     def plane_out(self, plane):
#         if (self.current_planes_nb ) > 0:
#             self.current_planes_nb -= 1
#             self.airplanes.remove(plane)
#             return True
#         else:
#             return False
#
#     def describe(self):
#         print("Airport {}: {}/{} planes".format(self.name,
#                                                 self.current_planes_nb,
#                                                 self.capacity))
#
#     def ui(self):
#
#         print("Hey, welcome to {} Airport".format(self.name))
#
#         while True:
#             print("\n\n")
#             print("What do you want to do? (Choose a number)")
#             print("0) Exit")
#             print("1) Add planes")
#             print("2) Remove planes")
#             print("3) Get airport status")
#
#             choice = input(">>> ")
#             if choice not in ["0", "1", "2", "3"]:
#                 print("Please enter 0, 1 or 2")
#                 continue
#
#             if choice == "0":
#                 print("Goodbye!")
#                 break
#
#             elif choice == "1":  # PLANE IN
#                 nb_of_planes = input("How many planes do you wanna add?\n>>> ")
#                 try :
#                     nb_of_planes = int(nb_of_planes)
#                 except:
#                     print("wrong number of planes")
#                     continue
#
#                 if self.plane_in(nb_of_planes):
#                     print("{} planes entered {}".format(nb_of_planes, self.name))
#                 else:
#                     print("Sorry, no more places available")
#
#             elif choice == "2":  # PLANE OUT
#                 nb_of_planes = input("How many planes do you wanna remove?\n>>> ")
#                 try:
#                     nb_of_planes = int(nb_of_planes)
#                 except:
#                     print("wrong number of planes")
#                     continue
#
#                 if self.plane_out(nb_of_planes):
#                     print("{} planes left from {}".format(nb_of_planes, self.name))
#                 else:
#                     print("You have no planes in your airport")
#
#             elif choice == "3":
#                 self.describe()
#
#
# class Plane:
#
#     plane_id = 0
#     nb_of_planes = 0
#     plane_map = {}
#
#     def __init__(self, model, color,fuel_capacity, fuel_cansumption_perkm, passangers_capacity, current_airport):
#
#         self.plane_id = Plane.plane_id
#
#         Plane.plane_id += 1
#         Plane.plane_map[Plane.plane_id] = self              # assigning value to the dictionary
#         Plane.nb_of_planes = len(Plane.plane_map)           # Counting the number of planes in the Airport
#
#         self.model = model
#         self.color = color
#         self.fuel_capacity =fuel_capacity
#         self.fuel_consumption_perkm = fuel_cansumption_perkm
#         self.passangers_capacity = passangers_capacity
#         self.current_airport = current_airport
#         self.current_fuel = 0
#
#
#     def __repr__(self):
#         return self.color,self.model,'currently in ',self.current_airport, "fuel Status",self.current_fuel,"/",self.fuel_capacity
#
#
#     def add_passangers(self, nb_passanger):
#         if nb_passanger > self.passangers_capacity:
#             print("sorry we don't have enough seats")
#             return False
#         else:
#             print("passamger received")
#             return True
#
#     def calculate_needed_fuel(self,distance):
#        return self.fuel_consumption_perkm * distance
#
#     def refill_fuel(self):
#         if self.current_fuel < self.fuel_capacity:
#             self.current_fuel = self.fuel_capacity
#             print("fuel refilled")
#
#     def fly(self, destination,departure, distance):
#         if self.calculate_needed_fuel(distance) > self.fuel_capacity:
#             print("sorry the plane can't handle this trip")
#             return False
#         if self.fuel_capacity > self.calculate_needed_fuel(distance) > self.current_fuel:
#             self.refill_fuel()
#         self.current_airport = departure
#
#
#
#
#             print("{} has departed from {} to {} and has travelled {} kms".format(self.model, self.current_airport, destination, distance))
#
#
#     def query(id):
#         print( Plane.plane_map[id])
#
#
#
#
#
#
#
#
# p1 = Plane("Boeing 777","blue", 200, 10, 100, 'Asmara Airport')
# p2 = Plane("Boeing 777","blue", 200, 10, 100, 'Asmara Airport')
# p3 = Plane("Boeing 777","blue", 200, 10, 100, 'Asmara Airport')
# p4 = Plane("Boeing 777","blue", 200, 10, 100, 'Asmara Airport')
# print(p1.__repr__())
# print(Plane.nb_of_planes)
#
#
#

def fact(x):
    if x == 0:
        return 1
    return fact(x)

x=int(input())
print(fact(x))