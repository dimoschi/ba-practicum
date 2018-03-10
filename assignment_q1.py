import os
import pandas as pd
import numpy as np
from datetime import datetime


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


def powerset(input_set):
    return None


def list_keys(input_dict, regex):
    return None
