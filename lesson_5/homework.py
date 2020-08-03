class Car:
    count_electric = 0
    count_diesel = 0
    def __init__(self, color, age):
        self.color = color
        self.age = age

    @classmethod
    def count_cars(cls):
        print('Electic cars', cls.count_electric)
        print('Diesel cars', cls.count_diesel)


class ElectricCar(Car):
    
    def __init__(self, color, age, **kwargs):
        Car.count_electric += 1
        self.fuel_type = kwargs.pop('fuel_type', 'li-on')
        super().__init__(color, age)


class DieselCar(Car):

    def __init__(self, color, age, **kwargs):
        Car.count_diesel += 1
        self.fuel_type = kwargs.pop('fuel_type', 'li-on')
        super().__init__(color, age)


e1 = ElectricCar('green', 22, fuel_type='baterie')
d1 = DieselCar('red', 10)
d2 = DieselCar('yellow', 3)

Car.count_cars()