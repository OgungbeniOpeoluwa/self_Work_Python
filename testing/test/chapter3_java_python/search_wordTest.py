import unittest

from chapter3_java_python import search_word


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        result = search_word.return_if_word_exist_in_dict (array, word)
        # print(search_word.return_letter_if_exist(array, word))
        self.assertTrue(result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
