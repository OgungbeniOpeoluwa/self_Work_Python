import unittest

from chapter3_java_python.HealthRecordMain import HealthRecord


class MyTestCase(unittest.TestCase):
    def test_something(self):
        health_record = HealthRecord("ayo", "joy", "june", "female", 1999, 20, 60, 50)
        health_record.first_name("ope")
        self.assertEqual("ope", health_record.get_first_name())
        health_record.last_name("joseph")
        self.assertEqual("joseph", health_record.get_last_name())
        health_record.gender("female")
        self.assertEqual("female", health_record.get_gender())
        health_record.month("july")
        self.assertEqual("july", health_record.get_month())
        health_record.year(1999)
        self.assertEqual(1999, health_record.get_year())
        health_record.date(10)
        self.assertEqual(10, health_record.get_date())
        health_record.height(55)
        self.assertEqual(55, health_record.get_height())
        health_record.weight(50)
        self.assertEqual(50, health_record.get_weight())

    def test_age_calculator(self):
        health_record = HealthRecord("ayo", "josef", "female", "july", 1999, 10, 44, 50)
        health_record.year(1999)
        self.assertEqual(1999, health_record.get_year())
        result = health_record.age_calculator(2023)
        self.assertEqual(24, result)

    def test_maximum_heart_rate(self):
        health_record = HealthRecord("ayo", "josef", "female", "july", 1999, 10, 45, 65)
        maximum = health_record.maximum_heart_rate(2023)
        self.assertEqual(196, maximum)

    def test_target_heart_rate(self):
        health_record = HealthRecord("ayo", "josef", "male", "july", 1999, 10, 65, 55)
        result = health_record.target_heart_rate(65, 85, 2023)
        self.assertEqual("127.4:166.6", result)

    def test_body_mass_index(self):
        health_record = HealthRecord("ayo", "josef", "male", "july", 1999, 10, 24, 200)
        result = health_record.body_mass_index()
        self.assertEqual("244.10", result)


if __name__ == '__main__':
    unittest.main()
