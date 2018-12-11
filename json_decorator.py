#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import collections
import data_filling


def json_decorator(func):
    def wrapper(array):
        if type(array) is str:
            array = json.loads(array)

        code = fill_level(array)
        if code == -1:
            result = "insufficient data"
        else:
            if code == 0:
                array = data_filling.filling_aver(array, False)  # TODO: fix?

            result = func(array)

        result = json.dumps(result)
        return code, result

    return wrapper


def fill_level(array):
    counter = collections.Counter(array)
    if counter["NaN"] == 0:
        return 1
    elif counter["NaN"] < len(array) / 2:
        return 0
    else:
        return -1
