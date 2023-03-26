class Volkswagen(object):

    def __init__(self, price, year, mileage, fuel):
        self.price = price
        self.year = year
        self.mileage = mileage
        self.fuel = fuel

    def clean_data(self):

        # Price
        text = self.price.replace(" ", "")
        text = text.replace("PLN", "")
        self.price = int(text)

        # Year
        self.year = int(self.year)

        # Mileage
        text = self.mileage.replace(" ", "")
        text = text.replace("km", "")
        self.mileage = int(text)

        # Fuel
        text = self.fuel.replace(" ", "")
        text = text.replace("cm3", "")
        self.fuel = int(text)

    def return_data(self):

        return ([self.price, self.year, self.mileage, self.fuel])



        

    
