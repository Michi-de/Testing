class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

def car_info(car):
    print("Make:", car.make)
    print("Model:", car.model)
    print("Year:", car.year)

my_car = car("Toyota", "Corolla", 2020)
car_info(my_car)
