class HealthRecord:
    def __init__(self, first_name, last_name, gender, month, year, date, height, weight):
        self._date = date
        self._year = year
        self._month = month
        self._gender = gender
        self._last_name = last_name
        self._first_name = first_name
        self._height = height
        self._weight = weight

    def first_name(self, name):
        self._first_name = name

    def get_first_name(self):
        return self._first_name

    def last_name(self, name):
        self._last_name = name

    def get_last_name(self):
        return self._last_name

    def month(self, month):
        self._month = month

    def get_month(self):
        return self._month

    def year(self, year):
        self._year = year

    def get_year(self):
        return self._year

    def date(self, date):
        self._date = date

    def get_date(self):
        return self._date

    age = 0

    def age_calculator(self, year):
        age = year - self._year
        return age

    def maximum_heart_rate(self, year):
        return 220 - self.age_calculator(year)

    def target_heart_rate(self, percentage, percentage2, year):
        result = self.maximum_heart_rate(year) * (percentage / 100)
        result2 = self.maximum_heart_rate(year) * (percentage2 / 100)
        if percentage >= 50 and percentage2 <= 85:
            return f'{result:.1f}:{result2:.1f}'
        elif percentage >= 65 and percentage2 <= 85:
            return f'{result:.1f}:{result2:.1f}'

    def height(self, height):
        self._height = height

    def get_height(self):
        return self._height

    def weight(self, weight):
        self._weight = weight

    def get_weight(self):
        return self._weight

    def gender(self, gender):
        self._gender = gender

    def get_gender(self):
        return self._gender

    def body_mass_index(self):
        total = (self._weight * 703) / (self._height * self._height)
        return f'{total:.2f}'
