# class Student:
    # pass
# student1 = Student()
# student2 = Student()
# student1.name ="Hari"
# student1.age = 23
# student2.name = "Pooja"
# student2.age = 22
# print(student1.name)
# print(student1.age)
# print(student2.name)
# print(student2.age)
# 
# class Student:
    # def __init__(self,name,age):
        # self.name = name
        # self.age = age
    # def introduce(self):
        # print("My name is ",self.name)
        # print("My age is ",self.age)
    # def study(self):
        # print(self.name," is studying")
    # def show_details(self):
        # print("Name :",self.name)
        # print("Age :",self.age)
# student1 = Student("Hari",23)
# student2 = Student("Pooja",22)
# student1.show_details()
# student2.show_details()
# student2.study()
# student1.introduce()
# student1.study()

# student1.age = 100 #--> without encapsulation we can change the attribute because it is curently public
# student1.show_details()  #--> So we use Encapsulation
# 
#  ENCAPSULATION
class Student:
    def __init__ (self,name,age):
        self.name = name
        self.__age =age
    def show_details(self):
        print("Name:",self.name)
        print("Age :",self.__age)
    def get_age(self):
      return self.__age
    def set_age(self,age):
        self.__age = age
    def set_age(self, age):
        if age > 0:
          self.__age = age
        else:
          print("Age must be positive")
student1 = Student("Hari",23)
student1.show_details()

# print(student1.__age) #--> now we cant use private attribute outside the class

# IF we really want to Use that attribute out side the we use " GETTER"
print(student1.get_age())

#   Next "SETTER"
student1.set_age(24)
print(student1.get_age())


student1.set_age(24)
print(student1.get_age())
student1.set_age(-5)
print(student1.get_age())

### INHERITANCE
## 1 Single inheritance:
class person:
   def introduction(self):
      print(" I am a person")
class Student(person):
   pass
student1 = Student()
student1.introduction()

##2. Multiple Inheritance:
class person:
   def introduction(self):
      print(" I am a person")
class Learner:
   def study(self):
      print("Iam Studying")
class Student(person, Learner):
   pass
student1 = Student()
student1.introduction()
student1.study()

# Multi Level Inheritence:
class Person:
   def introduction(self):
      print("I am Person")
class Student(Person):
   def study(self):
      print("I am studying")
class CollegeStudent(Student):
   def attend_class(self):
      print("I am attending college")
student1=CollegeStudent()
student1.introduction()
student1.study()
student1.attend_class()

# Hierarchical Inheritancce
class Person:
   def introduction(self):
      print("I am a person")
class Student(Person):
   def study(self):
      print("I am Studying")
class Teacher(Person):
   def teach(self):
      print("I am teaching")
student2 = Student()
teacher1 = Teacher()
student2.introduction()
student2.study()
teacher1.introduction()
teacher1.teach()

#  Hybrid Inheritance:
class Person:
   def introduction(self):
      print("I am a person")
class Student(Person):
   def study(self):
      print("I am Studying")
class Teacher(Person):
   def teach(self):
      print("I am teaching")
class CollegeStudent(Student,Teacher):
   def attend_class(self):
      print("I am attending college")

student3 = CollegeStudent()
student3.introduction()
student3.study()
student3.teach()
student3.attend_class()

##POLYMORPHISM##

class Dog:
   def sound(self):
      print("Dog Barks")
class Cat:
   def sound(self):
      print("Cat meows")
dog1 = Dog()
cat1 = Cat()
dog1.sound()
cat1.sound()

animals = [Dog(),Cat()]
for animal in animals:
   animal.sound()

#Method Overriding
class Person:
   def introduction(self):
      print("I am a person")
class Student(Person):
   def introduction(self):
      print("I am a Student")
person1 = Person()
student1 = Student()
person1.introduction()
student1.introduction()
# SUPER()
class Person:
   def introduction(self):
      print("I am a person")
class Student(Person):
   def introduction(self):
      super().introduction()
      print("I am a Student")
student1 = Student()
student1.introduction()
# DUCK TYPING
class Dog:
   def sound(self):
      print("Dog barks")
class Cat:
   def sound(self):
      print("Cat meows")
def make_sound(animal):
   animal.sound()
make_sound(Dog())
make_sound(Cat())

## Abstraction ##

from abc import ABC, abstractmethod
class Vehicle(ABC):
   @abstractmethod
   def start(self):
      pass


class Car:
   def start(self):
      print("Car starts with a key")
car1 = Car()
car1.start()
# combination of Abstraction and Polymorphism
class Vehicle(ABC):
   @abstractmethod
   def start(self):
      pass
class Car(Vehicle):
   def start(self):
      print("Car starts with a key")

class Bike(Vehicle):
   def start(self):
      print("Bike starts with button")
car1 = Car()
bike1 = Bike()
car1.start()
bike1.start()
## Class variable VS Intance Variable ##
#Instance variable
class Student:
   def __init__(self,age,Name):
      self.Name = Name
      self.age = age
student1 = Student(23,"Hari")
student2 = Student(22,"Pooja")
print(student1.Name)
print(student2.Name)
#class variable
class Student:
   school = "ABC school"

   def __init__(self,age,Name):
      self.Name = Name
      self.age = age
student1 = Student(23,"Hari")
student2 = Student(22,"Pooja")
print(student1.school)
print(student2.school)

Student.school = "XYZ school"
print(student1.school)
print(student2.school)

## @classmethod##
class Student:
   school = "ABC school"
   @classmethod
   def change_school(cls,new_school):
      cls.school = new_school
Student.change_school("HIJ school")
print(Student.school)

## @Static method ##
class Student:
   @staticmethod
   def welcome():
      print("Welcome to the Student class")

Student.welcome()

## Composition ##
class Engine:
   def start(self):
      print("Engine starts")

class Car:
   def __int__(self):
      self.engine = Engine()
# Here a car has an engine 
