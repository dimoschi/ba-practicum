import re


def is_palindrome(word):
    # str to force int to str and revers, need another implementation for float
    # TODO: Add float check & implementation
    return str(word) == "".join(reversed(str(word)))


def create_tuples(list_a, list_b):
    # Check for errors in input
    if len(list_a) != len(list_b):
        return "Lists are not equal"
    elif not isinstance(list_a, list) or not isinstance(list_b, list):
        return "Input is not list"

    results = set()
    for elem_a in list_a:
        for elem_b in list_b:
            results.add((elem_a, elem_b))
    return results


def get_power_set(input_set):
    # Empty set declared as frozenset
    power_set = [frozenset()]

    for element in input_set:
        new_sets = []
        for subset in power_set:
            new_sets.append(subset | set([element, ]))
        power_set.extend(frozenset(new_sets))

    return set(power_set)


def list_keys(input_dict, regex):
    try:
        pattern = re.compile(regex)
    except TypeError:
        print("Regular expression is not a string or a compiled pattern")
    keys_list = []
    for key in input_dict.keys():
        if pattern.match(key):
            keys_list.append(key)

    return keys_list
