class Flower():

    def __init__(self, flower_name: str = "Lilium", number_of_petals: int = 5, price: float = 3.14):
        self.flower_name = flower_name
        self.number_of_petals = number_of_petals
        self.price = price

    def get_flower_name(self):
        return self.flower_name

    def set_flower_name(self, flower_name):
        self.flower_name = flower_name

    def get_number_of_petals(self):
        return self.number_of_petals

    def set_number_of_petals(self, number_of_petals):
        self.number_of_petals = number_of_petals

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

