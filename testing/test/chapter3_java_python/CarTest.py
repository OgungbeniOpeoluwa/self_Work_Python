import unittest

from chapter3_java_python.CarMain import CarMain


class MyTestCase(unittest.TestCase):
    def test_something(self):
        my_car = CarMain("toyota", "2020", 500)
        my_car.set_model("camry")
        self.assertEqual("camry", my_car.get_model())
        my_car.set_year("2020")
        self.assertEqual("2020", my_car.get_year())
        my_car.set_price(50000)
        self.assertEqual(50000, my_car.get_price())

    def test_for_negative_price(self):
        my_car = CarMain("toyota", "2020", 500)
        my_car.set_price(50000)
        self.assertEqual(50000, my_car.get_price())
        my_car.set_price(-5000)
        self.assertEqual(50000, my_car.get_price())

    def test_for_discount_price(self):
        my_car = CarMain("toyota", "2020", 500)
        my_car2 = CarMain("toyota", "1996", 4500)
        my_car.set_price(50000)
        self.assertEqual(50000, my_car.get_price())
        my_car2.set_price(30000)
        self.assertEqual(30000, my_car2.get_price())
        my_car.discounted_price(5)
        self.assertEqual(47500, my_car.get_price())
        my_car2.discounted_price(7)
        self.assertEqual(27900, my_car2.get_price())


if __name__ == '__main__':
    unittest.main()
