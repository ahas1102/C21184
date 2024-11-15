class Bicycle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_age(self):
        return 2024 - self.year


bike = Bicycle(model='sport', brand='Scott',year=2010)
print(f"Возраст велосипеда: {bike.get_age()} лет")
