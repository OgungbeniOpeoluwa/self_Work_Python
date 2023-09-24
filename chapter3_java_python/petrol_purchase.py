class Purchase:
    def __init__(self, location, petrol_type, quantity_per_litter, price_per_litter, percent_discount):
        self._location = location
        self._petrol_type = petrol_type
        self._quantity_per_litter = quantity_per_litter
        self._price_per_litter = price_per_litter
        self._percent_discount = percent_discount

    def set_location(self, location):
        self._location = location

    def get_location(self):
        return self._location

    def set_petrol_type(self, petrol_type):
        self._petrol_type = petrol_type

    def get_petrol_type(self):
        return self._petrol_type

    def set_quantity_price_per_litter(self, price):
        self._quantity_per_litter = price

    def get_quantity_per_litter(self):
        return self._quantity_per_litter

    def set_price_per_litter(self, amount):
        self._price_per_litter = amount

    def get_price_per_litter(self):
        return self._price_per_litter

    def set_percentage_discount(self, percent):
        self._percent_discount = percent

    def get_percentage_discount(self):
        return self._percent_discount

    def purchase_amount(self):
        return (self._quantity_per_litter * self._price_per_litter) - (self._percent_discount / 100)


