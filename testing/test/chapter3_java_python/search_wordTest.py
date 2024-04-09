import unittest

from chapter3_java_python import search_word


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        result = search_word.return_if_word_exist_in_dict(array, word)
        self.assertTrue(result)

    def test_for_see(self):
        array = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        result = search_word.return_if_word_exist_in_dict(array, word)
        self.assertTrue(result)

    def test_for_ABCB(self):
        array = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
        word = "ABCEFSADEESE"
        result = search_word.return_if_word_exist_in_dict(array, word)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
