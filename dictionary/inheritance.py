class Phone():

    def __init__(self, brand, model, phone_number, tactile_screen=False):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number
        self.tactile_screen = tactile_screen

    def call(self, number_to_call):
        print("Calling to {}...".format(number_to_call))

    def txt_message(self, number, message):
        print("Sending to {}: {}".format(number, message))


class Smartphone(Phone):  # Specify that Smartphone inherit from Phone

    def __init__(self, brand, model, phone_number, nb_of_cameras):
        super().__init__(brand, model, phone_number, tactile_screen=True)  # super() is the parent function
        self.nb_of_cameras = nb_of_cameras

    def take_pic(self):
        print("Say cheese! *Click*")
        print("You took a picture with {} cameras".format(self.nb_of_cameras))

class Iphone(Smartphone):
    def __init__(self, brand, model, phone_number,camera_pixle, app_downloader):
        super().__init__(brand, model, phone_number,tactile_screen=True)
        self.camera_pixle = camera_pixle
        self.memory_size = 256

        self.app_downloader = app_downloader
    def itune_music(self):
        print("you are playing music from itune.")

    def downloder(self):
        if self.memory_size < 256:
            print("you are downloding ....")

        else:
            print("sorry you don't have enough spaces")



