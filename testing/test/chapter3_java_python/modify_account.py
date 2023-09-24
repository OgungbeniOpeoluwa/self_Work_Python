import unittest

from chapter3_java_python.bank_account import MyAccount


class MyTestCase(unittest.TestCase):
    def test_check_balance(self):
        account = MyAccount()
        self.assertEqual(0, account.get_balance())  # add assertion here

    def test_deposit(self):
        account = MyAccount()
        account.deposit(5000)
        self.assertEqual(5000, account.get_balance())

    def test_account_cant_deposit_negative_value(self):
        account = MyAccount()
        account.deposit(5000)
        self.assertEqual(5000, account.get_balance())
        account.deposit(-500)
        self.assertEqual(5000, account.get_balance())

    def test_withdraw(self):
        account = MyAccount()
        account.deposit(7000)
        self.assertEqual(7000, account.get_balance())
        account.withdrawal(1000)
        self.assertEqual(6000, account.get_balance())

    def test_display_account(self):
        account = MyAccount()
        account.deposit(7000)
        self.assertEqual(7000, acc)
        account.withdrawal(1000)
        self.assertEqual(6000, account.get_balance())

    def test_amount_withdraw_is_greater_than_balance(self):
        account = MyAccount()
        account.deposit(5000)
        self.assertEqual(5000, account.get_balance())
        account.withdrawal(10000)
        self.assertEqual(5000 , account.get_balance())


if __name__ == '__main__':
    unittest.main()
