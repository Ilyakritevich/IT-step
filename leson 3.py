class Human:

    def __init__(self, name):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self. passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_pasangers(self):
        if self.passengers != []:
            print(F"Names of {self.brand} pasanrgers:")
            for pasanger in self.passengers:
                print(pasanger.name)
        else:
            print(F"There are no pasangers in {self.brand} ")


Biber = Human("Biber")
Kate = Human("Kate")

auto = Auto("BMW")
auto.add_passenger(Kate)
auto.add_passenger(Biber)

auto.print_pasangers()
