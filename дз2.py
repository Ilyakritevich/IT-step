import time

class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.hunger = 50
        self.energy = 50

    def sleep(self, hours):
        print(f"{self.name} няшится протягом {hours} годин.")
        self.energy += 10 * hours
        time.sleep(hours)

    def eat(self, food):
        print(f"{self.name} хапає {food}.")
        self.hunger -= 10
        self.energy += 5

    def play(self, time):
        print(f"{self.name} грається {time} годин.")
        self.hunger += 5
        self.energy -= 10 * time


my_cat = Cat("Барсик", "сірий")

print(f"{my_cat.name} щасливий кіт {my_cat.color} кольору.")

my_cat.sleep(8)
my_cat.eat("рибу")
my_cat.play(2)
