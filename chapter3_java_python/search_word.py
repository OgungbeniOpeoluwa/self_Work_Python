def return_if_word_exist_in_dict(array, word: str):
    count = 0
    result = 0
    result2 = 0
    result3 = {}
    for letter in range(0, len(word)):
        l = word[letter]
        values = return_letter_if_exist(array, word[letter])
        result2 = values
        # print(result2)
        if result == 0:
            result = values
        else:
            for n in result:
                print(n)
                if array[n[0]][n[1]] == l:
                    if count > 1:
                        check_which_number_fit(result2)
                    count+=1
                    result3[l] = n
            result = result2

        print(result3)
    return result


def check_which_number_fit(array, words, letter):
   for n,u in array:
       print(n)
       print(u)
   return 0


def return_letter_if_exist(word, letter):
    value = []
    for n in range(0, len(word)):
        for r in range(0, len(word[n])):
            if word[n][r] == letter:
                if r <= len(word) - 1:
                    result = [n, r + 1]
                    value.append(result)
                if n - 1 >= 0:
                    values = n - 1
                    result = [n - 1, r]
                    value.append(result)
                if r - 1 >= 0:
                    values = r - 1
                    result = [n, r - 1]
                    value.append(result)
                if n + 1 <= len(word) - 1:
                    values = n + 1
                    result = [n + 1, r]
                    value.append(result)
                value.append([n, r])
    return value
