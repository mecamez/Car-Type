class Car:
    def __init__(self, type, brand, year):
        self.type = type
        self.brand = brand
        self.year = year

    def find_brand(self):
        if self.brand == 'Ford' or 'Chevrolet':
            print(f"Your {self.brand} veichle is American made!")

        if self.brand == 'Toyota' or 'Hyundai':
            print(f"Your {self.brand} veichle is Japanese made!")
        
        if self.brand == 'Audi' or 'Volkswagen':
            print(f"Your {self.brand} veichle is German made!")

    def find_year(self):
        if self.year >= 1990:
            print(f"Your {self.brand} veichle is considered a classic.")
        elif self.year >= 1990 <= 2000:
            print(f"Your {self.brand} veichle is considered a classic!")
        elif self.year >= 2000 <= 2010:
            print(f"Your {self.brand} veichle is considered modern!")
        elif self.year >= 2010:
            print(f"Your {self.brand} veichle is considered modern!")

if __name__ == "__main__":
    my_car = Car("Sedan", "Toyota", 2005)
