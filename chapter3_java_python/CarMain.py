class CarMain:

    def __init__(self, model, year, price):
        self._price = price
        self._year = year
        self._model = model

    def set_model(self, model):
        self._model = model

    def get_model(self):
        return self._model

    def set_year(self, year):
        self._year = year

    def get_year(self):
        return self._year

    def set_price(self, amount):
        if amount > 0:
            self._price = amount

    def get_price(self):
        return self._price

    def discounted_price(self, percent):
        self._price -= (self._price * (percent / 100))
