class Car:
    wheels = 4 # class variables
    def __init__(self, model, year, color, for_sale): # constructor method
        self.model = model # these are instance variable
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print(f"You drive the {self.model}")