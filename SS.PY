# Assignment 1: Design Your Own Class! 🏗️

class Smartphone:
    def __init__(self, brand, model, storage_gb):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_percentage = 100
        self.is_locked = True

    def call(self, number):
        if not self.is_locked:
            print(f"{self.brand} {self.model} is calling {number}...")
        else:
            print("Smartphone is locked. Unlock to make a call.")

    def take_photo(self):
        if not self.is_locked:
            print(f"{self.brand} {self.model} took a photo.")
        else:
            print("Smartphone is locked. Unlock to take a photo.")

    def install_app(self, app_name):
        if not self.is_locked:
            print(f"Installing {app_name} on {self.brand} {self.model}...")
        else:
            print("Smartphone is locked. Unlock to install apps.")

    def unlock(self):
        self.is_locked = False
        print(f"{self.brand} {self.model} unlocked.")

    def lock(self):
        self.is_locked = True
        print(f"{self.brand} {self.model} locked.")

    def get_battery_percentage(self):
        return f"Battery: {self.battery_percentage}%"

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, cooling_system):
        super().__init__(brand, model, storage_gb)
        self.cooling_system = cooling_system

    def play_game(self, game_title):
        if not self.is_locked:
            print(f"Playing {game_title} on {self.brand} {self.model} with {self.cooling_system} cooling.")
        else:
            print("Smartphone is locked. Unlock to play games.")

# Example Usage for Assignment 1
my_phone = Smartphone("Google", "Pixel 8", 128)
my_gaming_phone = GamingPhone("ASUS", "ROG Phone 7", 512, "Vapor Chamber")

my_phone.call("123-456-7890")
my_phone.unlock()
my_phone.call("123-456-7890")
my_phone.take_photo()
my_gaming_phone.play_game("Apex Legends Mobile")
print(my_phone.get_battery_percentage())
print(my_gaming_phone.get_battery_percentage())
my_phone.lock()
my_phone.install_app("Cool New Game")
my_gaming_phone.call("987-654-3210")

print("\n" + "="*30 + "\n")

# Activity 2: Polymorphism Challenge! 🎭

class Animal:
    def move(self):
        print("Animal moves in a generic way.")

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

def let_it_move(obj):
    obj.move()

# Example Usage for Activity 2
animal = Animal()
car = Car()
plane = Plane()

let_it_move(animal)
let_it_move(car)
let_it_move(plane)