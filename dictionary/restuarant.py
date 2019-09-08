
























# The restaurant

# A class Restaurant with those attributes:
#
# capacity --> int
# nb_of_tables --> int
# tables_state --> Dictionary {1:True, 2:False, 3:True... for every table}
# opening_hour --> int
# closing_hour --> int

#  methods:
#
# client_in --> if you can add them, return true and add them to a table,
#              but you have to check that the restaurant is open, arguments are
#              how many client want to get in and the hour
# client_out --> every clients of a table leave, the table is now free, arguments are which table is leaving


class Restaurant():

    def __init__(self,
                 name,
                 nb_of_tables,
                 opening_hour,
                 closing_hour
                 ):
        self.name = name
        self.nb_of_tables = nb_of_tables
        self.opening_hour = opening_hour
        self.closing_hour = closing_hour

        self.tables_state = {}  # False is empty and True is taken

        for i in range(self.nb_of_tables):
            self.tables_state[i] = False

    def describe(self):
        print("Welcome to the restaurant {}".format(self.name))

    def check_hour(self, hour):
        if self.opening_hour < hour < self.closing_hour == True:
            return True

    def free_table(self):
        for table_num in range(self.nb_of_tables):
            if self.tables_state[table_num] == False:
                return table_num
        return -1

    def Client_in(self, hour):
        # Check opening_hour
        if self.check_hour(hour) == False:
            print("Sorry, we're closed, we're opened only from {} to {}".format(self.opening_hour,
                                                                                self.closing_hour))
            return False

        # Check if there is a free table
        table_nb = self.free_table()
        if table_nb == -1:
            print("Sorry, no place available")
            return False

        print("You can come to table {}".format(table_nb))
        self.tables_state[table_nb] = True

    def table_out(self, table_nb):
        print("table {} has gone out".format(table_nb))
        self.tables_state[table_nb] = False

    def check_table(self, table_nb):
        return self.tables_state[table_nb] == False


restaurant = Restaurant("KFC", 20, 8, 18)
for _ in range(4):
    restaurant.Client_in(hour=15)
restaurant.table_out(1)
print(restaurant.free_table())
restaurant.check_table(1)

for table in range(2, 5):
    if restaurant.tables_state[table] == False:
        print("Table {} is empty".format(table))
    else:
        print("Table {} is taken".format(table))

print(restaurant.nb_of_tables)
print(restaurant.tables_state)















