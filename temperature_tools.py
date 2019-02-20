#!/usr/bin/python
# -*- coding: utf-8 -*-


import json
import math


def average_day(minimum, maximum):
    """Returns the average temperature per day"""

    if type(minimum) is str:
        minimum = float(minimum)

    if type(maximum) is str:
        maximum = float(maximum)

    if math.isnan(minimum) or math.isnan(maximum):
        return -1, "insufficient data"
    else:
        return 0, (minimum + maximum) / 2


def average_month(array):
    """Returns the average temperature for a month"""

    if type(array) is str:
        array = json.loads(array)

    known_numbers = list(filter(lambda x: not math.isnan(x), array))

    if len(known_numbers) < len(array) / 2:
        return -1, "insufficient data"
    else:
        return 0 if len(known_numbers) < len(array) else 1, sum(known_numbers) / len(known_numbers)


def average_daily_month(minimum, maximum):
    """Returns the average temperature per month based on the minimum and maximum temperatures of each day"""

    if type(minimum) is str:
        minimum = json.loads(minimum)

    code=1

    known_items=len(list(filter(lambda x: not math.isnan(x), minimum)))

    if known_items==len(minimum):
        code=1

    elif known_items>=len(minimum)/2:
        code=0
    else:
        return -1, "insufficient data"

    if type(maximum) is str:
        maximum = json.loads(maximum)

    known_items = len(list(filter(lambda x: not math.isnan(x), maximum)))

    if known_items>= len(maximum)/2:
        code=0
    elif known_items< len(maximum)/2:
        return -1, "insufficient data"


    aver = [average_day(minimum[i], maximum[i])[1] for i in range(max(len(minimum), len(maximum)))]

    return code, average_month(aver)
