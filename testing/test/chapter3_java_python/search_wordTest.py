import unittest

from chapter3_java_python.search_word import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        search_board = Solution()
        array = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        result = search_board.return_if_word_exist_in_dict(array, word)
        self.assertTrue(result)

    def test_for_see(self):
        search_board = Solution()
        array = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        result = search_board.return_if_word_exist_in_dict(array, word)
        self.assertTrue(result)

    def test_for_ABCEFSADEESE(self):
        search_board = Solution()
        array = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
        word = "ABCEFSADEESE"
        result = search_board.return_if_word_exist_in_dict(array, word)
        self.assertTrue(result)

    def test_for_ABCB(self):
        search_board = Solution()
        array = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        result = search_board.return_if_word_exist_in_dict(array, word)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
