# this example also show cases the use of multi level inheritance

class Animal:
    def eat(self):
        print("This animal eats.")
    def sleep(self):
        print("This animal sleeps.")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # multiple inheritance
    pass

rabbit = Rabbit()
hawk  = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

fish.flee()
fish.hunt()

rabbit.eat()