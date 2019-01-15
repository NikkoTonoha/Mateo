#!/usr/bin/python
# -*- coding: utf-8 -*-


import collections
import math
from functools import reduce
import json


def filling_aver(array, format_json=True):
    """Fills the missing values ​​by a mean value

    Keyword arguments:
    array - input data array
    format_json - determines whether to return to JSON format or list

    """

    if type(array) is str:
        array = json.loads(array)

    full = list(filter(lambda x: not math.isnan(x), array))

    aver = sum(full) / len(full)

    result = filling(array, aver)
    return json.dumps(result) if format_json else result


def filling_mode(array):
    """Fills the missing values ​​by a mode"""

    if type(array) is str:
        array = json.loads(array)
    counters = collections.Counter(array)

    mode = reduce(lambda a, x: x if math.isnan(a) or not math.isnan(x) and counters[x] > counters[a] else a, counters.keys())

    return json.dumps(filling(array, mode))


def filling_median(array):
    """Fills the missing values ​​by a median"""

    if type(array) is str:
        array = json.loads(array)
    array_sorted = sorted(list(filter(lambda x: not math.isnan(x), array)))
    if len(array_sorted) % 2 == 0:
        median = (array_sorted[int(len(array_sorted) / 2)] + array_sorted[int(len(array_sorted) / 2 - 1)]) / 2
    else:
        median = array_sorted[int(len(array_sorted) / 2)]

    return json.dumps(filling(array, median))


def filling(array, value):
    return list(map(lambda x: float(x) if not math.isnan(x) else float(value), array))


def filling_grouping(array):
    """Filling in missed values ​​by average values ​​using data grouping"""

    if type(array) is str:
        array = json.loads(array)

    full = filling_aver(array, False)
    size = int((len(array) + 1) / 2)

    while size >= 2:
        temp = []

        for i in range(0, len(array), size):
            temp += filling(array, sum(full[i:i + size]) / len(full[i:i + size]))

        full = temp

        size = int((size + 1) / 2)

    return json.dumps(full)
