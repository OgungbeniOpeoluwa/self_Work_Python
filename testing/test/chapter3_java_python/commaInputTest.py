import unittest

from chapter3_java_python import CommaInput


class MyTestCase(unittest.TestCase):
    def test_something(self):
        value = CommaInput.returnValueInAList()
        print(value)
        self.assertEqual([4, 9, 25], value)  # add assertion here


if __name__ == '__main__':
    unittest.main()
