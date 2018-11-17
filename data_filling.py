import collections
import math
from functools import reduce


def filling_aver(array):
    full = list(filter(lambda x: not math.isnan(x), array))

    aver = sum(full) / len(full)

    return filling(array, aver)


def filling_mode(array):
    counters = collections.Counter(array)

    if math.nan in counters:
        del counters[math.nan]

    mode = reduce(lambda a, x: x if counters[x] > counters[a] and not math.isnan(x) else a, counters)

    return filling(array, mode)


def filling_median(array):
    array_sorted = sorted(list(filter(lambda x: not math.isnan(x), array)))
    if len(array_sorted) % 2 == 0:
        median = (array_sorted[int(len(array_sorted) / 2)] + array_sorted[int(len(array_sorted) / 2 - 1)]) / 2
    else:
        median = array_sorted[int(len(array_sorted) / 2)]

    return filling(array, median)


def filling(array, value):
    return list(map(lambda x: x if not math.isnan(x) else value, array))


def filling_grouping(array):
    full = filling_aver(array)
    size = int((len(array) + 1) / 2)
    while size >= 2:
        temp = []

        for i in range(0, len(array), size):
            temp += filling(array, sum(full[i:i + size]) / len(full[i:i + size]))

        full = temp

        size = int( (size + 1) / 2)

    return full

