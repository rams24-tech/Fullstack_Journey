class Animal():
    def __init__(self,name,species,age):
        self.name=name
        self.species=species
        self.age=age
    def describe(self):
        print(f"{self.name} | Species: {self.species} | Age: {self.age}")

    def speak(self):
        print("some sound")

class Dog(Animal):
    def __init__(self,name,species,age,breed):
        super().__init__(name,species,age)
        self.breed=breed
    def speak(self):
        print(f"{self.name} says Woof!")
    def describe(self):
        super().describe()
        print(f"Breed: {self.breed}")   

class Cat(Animal):
    def __init__(self,name,species,age,color):
        super().__init__(name,species,age)
        self.color=color
    def speak(self):
        print(f"{self.name} says Meow! ")  
    def describe(self):
        super().describe()
        print(f"Color: {self.color}")                    


d1 = Dog("Bruno", "Mammal", 3, "Labrador")
c1 = Cat("Whiskers", "Mammal", 2, "White")

d1.describe()
d1.speak()
c1.describe()
c1.speak()
