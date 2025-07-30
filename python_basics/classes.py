class Vehicle:
    def __init__(self, brand, doors, wheels=3):
        self.brand = brand
        self.doors = doors
        self.wheels = wheels

    def car_greetings(self, local_slang):
        print(f"{local_slang}, I'm your new card, my name is {self.brand} and I have {self.wheels} wheels")


veh1 = Vehicle("vw", 2, 3)
print(veh1.brand, veh1.doors, veh1.wheels)
veh1.car_greetings('Ya')

veh2 = Vehicle("BMW", 4)
print(veh2.brand, veh2.doors, veh2.wheels)
veh2.car_greetings('Hi')


class Car:
    brand = "Volvo"


car1 = Car()
print(car1.brand)

car2 = Car()
print(car2.brand)
