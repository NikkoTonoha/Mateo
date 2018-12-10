#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import math
import functools


def maximum(array):
    """Returns the maximum value"""

    if type(array) is str:
        array = json.loads(array)

    return max(array)


def minimum(array):
    """Returns the minimum value"""

    if type(array) is str:
        array = json.loads(array)

    return min(array)


def average(array):
    """Returns the average value"""

    if type(array) is str:
        array = json.loads(array)

    return sum(array) / len(array)


def standard_deviation(array):
    """Returns the mean of the sample rejection"""

    if type(array) is str:
        array = json.loads(array)

    aver = average(array)
    sum = functools.reduce(lambda x, y: x+y,  map(lambda x: (x-aver)**2, array))

    return math.sqrt(sum / (len(array) - 1))


def swing_variation(array):
    """Returns the swing of variations"""

    return maximum(array)-minimum(array)

