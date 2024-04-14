import re
import datetime


class Solution:
    def return_if_word_exist_in_dict(self, dictionary, search_word: str):
        value = []
        values = []
        for n in search_word:
            if len(value) == 0:
                value = self.check_if_word_exist(n, dictionary, value)
                values.append(value)
                continue
            elif len(value) != 0:
                value = self.check_for_the_next_letter(n, dictionary, value)
                print(value)
                if self.check_if_list_already_exist(values, value):
                    array = self.check_array(values, dictionary, n, value)
                    if len(array) == 0:
                        return False
                values.append(value)
            else:
                # print(values)
                return False
        # print(values)
        return True

    def check_if_word_exist(self, letter, word, existed_array):
        for n in range(0, len(word)):
            for m in range(0, len(word[n])):
                if len(existed_array) != 0:
                    if n == existed_array[0] and m == existed_array[1]:
                        continue
                if word[n][m] == letter:
                    return [n, m]
        return []

    def check_for_the_next_letter(self, letter, dictionary, word):
        value1 = word[0]
        value2 = word[1]
        if value1 >= 0 and value1 < len(dictionary):
            n = value1 + 1
            if n < len(dictionary):
                if dictionary[n][value2] == letter:
                    return [n, value2]
                elif dictionary[value1 - 1][value2] == letter:
                    return [value1 - 1, value2]
        if value2 >= 0 and value2 < len(dictionary[value1]):
            n = value2 + 1
            if n < len(dictionary[value1]):
                if dictionary[value1][n] == letter:
                    return [value1, n]
                elif dictionary[value1][value2 - 1] == letter:
                    return [value1, value2 - 1]

        value = self.check_if_word_exist(dictionary[value1][value2], dictionary, word)
        if len(value) != 0:
            return self.check_for_the_next_letter(letter, dictionary, value)

    def check_if_list_already_exist(self, values, value):
        for n in values:
            if n == value:
                print(n)
                return True
        return False

    def check_array(self, values, dictionary, letter, value):
        check_value = values[len(values)-1]
        value1 = check_value[0]
        value2 = check_value[1]
        result = []
        if value1 >= 0 and value1 < len(dictionary):
            n = value1 + 1
            if n < len(dictionary):
                if dictionary[n][value2] == letter:
                    array = [n, value2]
                    if array != value:
                        return array
                elif dictionary[value1 - 1][value2] == letter:
                    array = [value1 - 1, value2]
                    if array != value:
                        return array
        if value2 >= 0 and value2 < len(dictionary[value1]):
            n = value2 + 1
            if n < len(dictionary[value1]):
                if dictionary[value1][n] == letter:
                    array = [value1, n]
                    if array != value:
                        return array
                elif dictionary[value1][value2 - 1] == letter:
                    array = [value1, value2 - 1]
                    if array != value:
                        return array
        return result
