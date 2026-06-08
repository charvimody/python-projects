class Vehicle:
    def start(self):
        print("Vehicle starts")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
my_car = Car()
my_car.start()
my_car.drive()
print("------------------")
class Person:
    def show_name(self):
        print("My name is charvi")
student1 = Person()
student1.show_name()
class Student(Person):
    def show_grade(self):
        print("Grade: A")
student1 = Student()
student1.show_grade()
print("------------------")
class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Bark")
cat = Cat()
dog = Dog()
cat.sound()
dog.sound()
print("------------------")
class Circle:
    def draw(self):
        print("Drawing Circle")
class Square:
    def draw(self):
        print("Drawing Square")
c = Circle()
s = Square()
c.draw()
s.draw()
print("------------------")
class Bird:
    pass
class Parrot(Bird):
    def speak(self):
        print("Parrot says Hello")
class Crow(Bird):
    def speak(self):
        print("Crow says Caw Caw")
parrot = Parrot()
crow = Crow()
parrot.speak()
crow.speak()