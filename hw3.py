class Human:
    def __init__(self, name):
        self.name = name
        self.car = None

    def buy_car(self, car):
        self.car = car
        print(f"{self.name} придбав(ла) автомобіль {car.brand} {car.model}")

    def drive(self):
        if self.car:
            print(f"{self.name} водить автомобіль {self.car.brand} {self.car.model}")
        else:
            print(f"{self.name} не має автомобіля")


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


john = Human("John")
honda = Car("Honda", "Civic")


john.buy_car(honda)


john.drive()