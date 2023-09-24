import unittest

from chapter3_java_python.petrol_purchase import purchase


class PetrolPurchaseTest(unittest.TestCase):
    def test_something(self):
        mine_purchase = purchase("yaba", "petrol", 500, 200, 20)
        mine_purchase.set_location("yaba")
        self.assertEqual("yaba", mine_purchase.get_location())
        mine_purchase.set_petrol_type("kerosene")
        self.assertEqual("kerosene", mine_purchase.get_petrol_type())
        mine_purchase.set_quantity_price_per_litter(5)
        self.assertEqual(5, mine_purchase.get_quantity_per_litter())
        mine_purchase.set_price_per_litter(500)
        self.assertEqual(500, mine_purchase.get_price_per_litter())
        mine_purchase.set_percentage_discount(20)
        self.assertEqual(20, mine_purchase.get_percentage_discount())

    def test_net_purchase(self):
        mine_purchase = purchase("yaba", "petrol", 500, 200, 20)
        mine_purchase.set_quantity_price_per_litter(50)
        self.assertEqual(50, mine_purchase.get_quantity_per_litter())
        mine_purchase.set_price_per_litter(500)
        self.assertEqual(500, mine_purchase.get_price_per_litter())
        mine_purchase.set_percentage_discount(10)
        self.assertEqual(10, mine_purchase.get_percentage_discount())
        result = mine_purchase.purchase_amount()
        self.assertEqual(24999.9, result)


if __name__ == '__main__':
    unittest.main()
