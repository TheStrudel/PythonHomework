import math


def change_quotes(string: str) -> str:
    for index, symbol in enumerate(string):
        if symbol == "\'":
            string = string[:index] + '\"' + string[index+1:]
        elif symbol == '\"':
            string = string[:index] + '\'' + string[index+1:]
    return string


def change_quotes_via_list(string: str) -> str:
    list_string = list(string)
    for index, symbol in enumerate(list_string):
        if list_string[index] == "\'":
            list_string[index] = '\"'
        elif list_string[index] == '\"':
            list_string[index] = '\''
    return "".join(list_string)


def is_palindrome(string: str) -> bool:
    for index in range(len(string)//2):
        if string[index] != string[-index-1]:
            return False
    return True


def my_split(string: str, splitter: str = ' ') -> list:
    words_list = []
    previous_index = 0
    while previous_index >= 0:
        index = string.find(splitter, previous_index)
        if index < 0:
            break
        words_list.append(string[previous_index:index])
        previous_index = index+1
    words_list.append(string[previous_index:])
    return words_list


def split_by_index(string: str, split_positions: list) -> list:
    words_list = []
    previous_position = 0
    for position in split_positions:
        if position > len(string) or position < previous_position:
            break
        words_list.append(string[previous_position:position])
        previous_position = position
    words_list.append(string[previous_position:])
    return words_list


def get_digits(number: int) -> tuple:
    digits = ()
    number = abs(number)
    if number == 0:
        return 0,
    for i in range(int(math.log10(number))+1):
        digits = digits + (number % 10, )
        number //= 10
    return digits[::-1]


def get_longest_word(string: str) -> str:
    words = string.split()
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def multiply_except_current(numbers: list) -> list:
    accumulation = 1
    multiplied = []
    for number in numbers:
        accumulation *= number
    for number in numbers:
        multiplied.append(int(accumulation/number))
    return multiplied


def get_pairs(lst: list) -> list:
    index = 1
    pairs = []
    while index < len(lst):
        pairs.append((lst[index-1], lst[index]))
        index += 1
    return pairs
