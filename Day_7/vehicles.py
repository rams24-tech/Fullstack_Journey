class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

    def describe(self):
        print(f"Brand: {self.brand} | Speed: {self.speed} kmph")


class Car(Vehicle):
    def __init__(self,brand,speed,num_doors):
        super().__init__(brand,speed)
        self.num_doors=num_doors

    def describe(self):
        print(f"Car - Brand: {self.brand} | Speed: {self.speed} kmph | Doors: {self.num_doors}")

class Truck(Vehicle):
    def __init__(self,brand,speed,cargo_tons):
        super().__init__(brand, speed)
        self.cargo_tons=cargo_tons

    def describe(self):
        print(f"Truck - Brand: {self.brand} | Speed: {self.speed} kmph | Cargo: {self.cargo_tons} tons")

c1=Car("i20",220,5)
t1=Truck("Verna",250,20) 

c1.describe()
t1.describe()
