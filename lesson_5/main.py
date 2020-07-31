#class example
class MyClass:

    a = 5
    b = 10

    def get(self):
        return self.a

    def set(self, value):
        self.a = value

a = MyClass()
print(a.a)
print(a.get())
a.set(10)
print(a.a)
a.a = 20
print(a.a)

b = MyClass()
b.a = 33
print(b.a)

print(MyClass.a, 'MyClass')

#class attributes
class MyClass:
    attr = 5

a = MyClass()
print(hasattr(a, 'attr'))
print(hasattr(a, 'attr1'))

x = getattr(a, 'attr')
y = getattr(a, 'attr1', 10)

setattr(a, 'attr', 10)
setattr(a, 'attr1', 20)
print(a.attr, a.attr1)


#instance method
class MyClass:

    def add_five(self, value):
        return value + 5

a = MyClass()
print(MyClass.add_five(10))

#class methond
class MyClass:

    @classmethod
    def sum(cls, value):
        return value + 5

print(MyClass.sum(10))


from datetime import date

class Person:

    age = 22

    @classmethod
    def age_by_year(cls, year):
        cls.age = date.today().year - year
a = Person()
print(a.age)
Person.age_by_year(1999)

b = Person()
print(b.age)

#staticmethod
from datetime import date

class Person:

    def __init__(self, age=44):
        self.age = age

    @staticmethod
    def calculate_age_by_year(year):
        return date.today().year - year

    @classmethod
    def age_by_year(cls, year):
        return cls(cls.calculate_age_by_year(year))
a = Person()
b = Person.age_by_year(1997)
print(Person.calculate_age_by_year(1995))


#Class attributes 
class Car:

    age = 10

car1 = Car()
Car.age = 20
car2 = Car()
print(car1.age, car2.age)

#Class attributes
class Car:

    def __init__(self, age=10):
        self.age = age

car1 = Car()
car2 = Car(20)
print(car1.age, car2.age)

#Class attributes
class Car:

    age = 44
    color = 'green'

    def __init__(self, age=20):
        self.age = age

car1 = Car()
car2 = Car(33)

print(car1.age, car2.age, Car.age)
print(car1.color, car2.color)


#Class / static / instance methods arguments
class Car:

    @classmethod
    def car_class_method(*args):
        print(args, 'car_class_method')

    @staticmethod
    def car_static_method(*args):
        print(args, 'car_static_method')

    def instance_method(*args):
        print(args, 'instance_method')



c = Car()
Car.car_class_method()
c.instance_method()
Car.car_static_method()
Car.car_static_method(10)

# Exercise 
from datetime import date

class Car:

    def __init__(self, year=2020, fuel='gasoline', color):
        self.year = year
        self.fuel = fuel
        self.color = color

    def age_of_car(self):
        print(date.today().year - self.year)

    def show_fuel_type(self):
        print(self.fuel)

    def update_color(self, color):
        self.color = color

c = Car(2009, 'diesel', 'green')
c.age_of_car()
c.show_fuel_type()
c.update_color('red')
print(c.color)


#operator overide 
class Person:

    count = 0

    def __init__(self, age=22):
        self.age = age
        Person.count += 1

    def __del__(self):
        Person.count -= 1

c = Person()
c1 = Person(22)
c2 = Person(33)

print(Person.count)

del c

print(Person.count)

#operator overide
class Car:

    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"This is car of age {self.age}"

    def __add__(self, value):
        self.age += value



c = Car(22)
print(c)

c.__add__(10)
c + 1
print(c.age)

#operator overide
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b)

    def __str__(self):
        return f'{self.a}, {self.b}'

c = Complex(10, 20)
c1 = Complex(30, 40)
c3 = c1 + c
print(c3)


#inheritance
class Parent:

    color = 'red'

    def implicit(self):
        print("Parent implicit")

    def override(self):
        print("Parent override")

    def altered(self):
        print('Parent atlered')

class Child(Parent):
    age = 10
    
    def override(self):
        print("Child override")
    
    def altered(self):
        print('Child, before Parent atlered')
        super().altered()
        print('Child, after Parent atlered')

p = Parent()
c = Child()
print(p.color, c.color)
print(c.age)
p.implicit()
c.implicit()

p.override()
c.override()
p.altered()
c.altered()


class Person:

    def __init__(self, age):
        self.age = age


class Employee(Person):

    def __init__(self, age, **kwargs):
        self.salary = kwargs.pop('salary', None)
        super().__init__(age)

e = Employee(10, salary=100)
print(e.age, e.salary)