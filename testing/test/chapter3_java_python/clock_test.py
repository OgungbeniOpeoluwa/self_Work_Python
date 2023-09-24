import unittest

from chapter3_java_python.ClockMain import ClockMain


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_clock = ClockMain(10, 35, 40)
        my_clock.set_hour(6)
        self.assertEqual(6, my_clock.get_hour())
        my_clock.set_minutes(10)
        self.assertEqual(10, my_clock.get_minutes())
        my_clock.set_second(8)
        self.assertEqual(8, my_clock.get_second())

    def test_that_hour_is_not_more_than24(self):
        my_clock = ClockMain(20, 10, 13)
        my_clock.set_hour(15)
        self.assertEqual(15, my_clock.get_hour())
        my_clock.set_hour(30)
        self.assertEqual(15, my_clock.get_hour())

    def test_that_minutes_is_not_more_than59(self):
        my_clock = ClockMain(20, 10, 13)
        my_clock.set_minutes(30)
        self.assertEqual(30, my_clock.get_minutes())
        my_clock.set_minutes(60)
        self.assertEqual(30, my_clock.get_minutes())

    def test_that_second_is_not_more_than59(self):
        my_clock = ClockMain(20, 10, 13)
        my_clock.set_minutes(30)
        self.assertEqual(30, my_clock.get_minutes())
        my_clock.set_hour(60)
        self.assertEqual(30, my_clock.get_minutes())

    def test_that_second_is_not_more_than59(self):
        my_clock = ClockMain(20, 10, 13)
        my_clock.set_second(15)
        self.assertEqual(15, my_clock.get_second())
        my_clock.set_second(60)
        self.assertEqual(15, my_clock.get_second())

    def test_display_time(self):
        my_clock = ClockMain(20, 10, 13)
        my_clock.set_hour(15)
        self.assertEqual(15, my_clock.get_hour())
        my_clock.set_minutes(30)
        self.assertEqual(30, my_clock.get_minutes())
        my_clock.set_second(15)
        self.assertEqual(15, my_clock.get_second())
        result = my_clock.display_time()
        self.assertEqual('15:30:15', result)


if __name__ == '__main__':
    unittest.main()
