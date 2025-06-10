# object = A "bundle" of related attributes (variables) and methods (functions)
# class = used to design the structure and layout of an object

from car import Car


car1 = Car("Mustang", "2025", "Black", True)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()

car2 = Car("Lamborgini", "2025", "Black", True)
print(car2.model)
print(car1.year)
print(car2.color)
print(car2.for_sale)