print("______This Is Inherentance______")
class Animal:

    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Animals make sounds")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
animalname = input("Enter animal name: ")
dog1 = Dog(animalname)
print("Animal Name:", dog1.name)
dog1.sound()
dog1.bark()
print("------------------------------------")
print("_____Now It Is Polymorphisum_____")
class cat:
   
    def sound(self):
        print("Cat says Meow")
class Dog:
    def sound(self):
        print("Dog says Bark")
c = cat()
d = Dog()
animals = [c, d]
for animal in animals:
    animal.sound()
print("------------------------------------")