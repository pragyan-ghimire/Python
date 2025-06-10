class Car:
    def __init__(self, model, year, color, for_sale): # constructor method
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print(f"You drive the {self.model}")