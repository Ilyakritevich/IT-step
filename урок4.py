#class GrantParent:
   # height = 180
   # eyes = "blue"

#class Parent(GrantParent):
   # height = 185
   # eyes = "brown"
   # def __init__(self):
       # print(F"Parent height: {self.height}")



#class Child(Parent):
   # height = 188
   # def __init__(self):
       # print(F"Child height: {self.height}")
        #print(F"Child eyes: {self.eyes}")


#Biber = Child()



#class Hallo:
#   def __init__(self):
#       print("Hallo")


#class HalloWorld(Hallo):
#   def __init__(self):
#        super().__init__()
#         print("World")


#hallo_world = HalloWorld()




class Computer:
    def __init__(self):
        self.mamory = 128
        self.ram = 8


class Display:

    def __init__(self):
        super().__init__()
        self.resolution = "4K"
        self.ram = 8


class Phone(Display,Computer):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def Display(self):
        print(F"Ram:{self.ram}")
        print(F"Memory:{self.mamory}")
        print(F"resolution:{self.resolution}")
        print(F"Child Name: {self.name}")

iphone14 = Phone



class Animal:
    def __init__(self):
        self.sleep = "100"
        self.hungry = "10 "
        self.power = "50"
        self.speed = "50"


class cat(Animal):
    def __init__(self):




















