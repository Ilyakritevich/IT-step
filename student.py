import random

class Student:
    def __init__(self, name,height):
        self.height = height
        self.name = name
        self.gladnes = 60
        self.alive = True
        print(f"hi.my name is {self, name}. my height is {self, height}")
    def to_study( self ):
        print("Time to study")
        self.progress += 0.1
        self.gladnes -= 5


    def to_chill(self):
        print("Reset time")
        self.progress += 0.12
        self.gladness -= 0.5

    def to_sleep(self):
        print("i sleep")
        self.gladnes += 5
    def to_alive(self):
     if self.progress < -0.5:
        print("Cast out...")
        self.alive = False
     elif self.gladness <= 0:
         print("Depression...")
        self.alive = False
     elif self.gladness > 5:
        print("Passed externally...")
         self.alive = False

    def end_of_day(self):
       print(f"gladness = {self.gladness}")
       print(f"progress = {round(self.progress, 2)}")


    def live(self, day):
       day = "Day" + str(day) + " of " + self.name + " life"
       print(f" {day:=^50}")

       choice = random. randint(  4,  3)

       if choice == 1:
            self.to_study()
       elif choice == 2:
            self.to_chill()
       else:
            self.to_sleep()






