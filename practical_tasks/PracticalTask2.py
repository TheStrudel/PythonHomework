import string


def appear_in_all_strings(*args: str) -> set:
    result = set(args[0])
    for arg in args[1:]:
        result.intersection_update(set(arg))
    return result if result else None


def appear_in_one_string(*args: str) -> set:
    result = set()
    for arg in args:
        result |= set(arg)
    return set(sorted(result))


def appear_in_two_strings(*args: str) -> set:
    all_letters = {}
    for arg in args:
        letters = set(arg)
        for element in letters:
            all_letters[element] = all_letters[element]+1 if element in all_letters else 0
    return set(element for element in all_letters if all_letters[element] > 0)


def do_not_appear_in_strings(*args: str) -> set:
    letters = set()
    for arg in args:
        letters |= set(arg.lower())
    return set(sorted(set(string.ascii_lowercase) - letters))


def generate_squares(number: int) -> dict:
    abs(number)
    squares = {num: num*num for num in range(1, number + 1)}
    return squares


def count_letters(args: str) -> dict:
    result = {}
    for letter in args:
        if letter not in result:
            result[letter] = 1
        else:
            result.update({letter: result[letter]+1})
    return result


def combine_dicts(*dictionaries: dict) -> dict:
    result = {}
    for dictionary in dictionaries:
        for key in dictionary.keys():
            if key in result:
                result.update({key: dictionary[key]+result[key]})
            else:
                result.update({key: dictionary[key]})
    return result


print(appear_in_two_strings())
