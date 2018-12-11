#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import functools
from json_decorator import json_decorator


@json_decorator
def maximum(array):
    """Returns the maximum value"""

    return max(array)

@json_decorator
def minimum(array):
    """Returns the minimum value"""

    return min(array)

@json_decorator
def average(array):
    """Returns the average value"""

    return sum(array) / len(array)

@json_decorator
def standard_deviation(array):
    """Returns the mean of the sample rejection"""

    aver = float(average(array)[1])
    sum = functools.reduce(lambda x, y: x+y,  map(lambda x: (x-aver)**2, array))

    return math.sqrt(sum / (len(array) - 1))

@json_decorator
def swing_variation(array):
    """Returns the swing of variations"""

    return max(array)-min(array)

