class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def bark(self):
        print("The Dog Barks.")


class Cat(Animal):
    def meow(self):
        print("The cat meows.")

dog = Dog("Tiger")
cat = Cat("Garfield")

print(f"The dog name is {dog.name}. It is {dog.is_alive}")
dog.bark()
print(f"The cat name is {cat.name}. It is {cat.is_alive}")
cat.meow()