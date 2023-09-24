class HeartRateCalculator:
    def __init__(self, first_name, last_name, month, year, date):
        self._date = date
        self._year = year
        self._month = month
        self._last_name = last_name
        self._first_name = first_name

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
