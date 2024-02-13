class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1,car2,car3 = Car("BMW","M5",2020),Car("BMW","X5",2018),Car("Tesla","Model 3",2020)

cars = [car1,car2,car3]

for car in cars:
    print(f'{car.make} {car.model} {car.year}')