import unittest

from chapter3_java_python.HeartRateCalCulator import HeartRateCalculator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        heart_rate = HeartRateCalculator("ayo", "joy", "june", 1999, 20)
        heart_rate.first_name("ope")
        self.assertEqual("ope", heart_rate.get_first_name())
        heart_rate.last_name("joseph")
        self.assertEqual("joseph", heart_rate.get_last_name())
        heart_rate.month("july")
        self.assertEqual("july", heart_rate.get_month())
        heart_rate.year(1999)
        self.assertEqual(1999, heart_rate.get_year())
        heart_rate.date(10)
        self.assertEqual(10, heart_rate.get_date())

    def test_age_calculator(self):
        heart_rate = HeartRateCalculator("ayo", "josef", "july", 1999, 10)
        heart_rate.year(1999)
        self.assertEqual(1999, heart_rate.get_year())
        result = heart_rate.age_calculator(2023)
        self.assertEqual(24, result)

    def test_maximum_heart_rate(self):
        heart_rate = HeartRateCalculator("ayo", "josef", "july", 1999, 10)
        maximum = heart_rate.maximum_heart_rate(2023)
        self.assertEqual(196, maximum)

    def test_target_heart_rate(self):
        heart_rate = HeartRateCalculator("ayo", "josef", "july", 1999, 10)
        result = heart_rate.target_heart_rate(65, 85, 2023)
        self.assertEqual("127.4:166.6", result)


if __name__ == '__main__':
    unittest.main()
