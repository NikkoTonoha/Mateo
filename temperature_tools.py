import math


def average_day(min, max):
    if math.isnan(min) or math.isnan(max):
        return -1, "insufficient data"
    else:
        return 0, (min + max) / 2


def average_month(temp):
    known_numbers = list(filter(lambda x: not math.isnan(x), temp))

    if  len(known_numbers)<len(temp)/2:
        return -1, "insufficient data"
    else:
        return 0 if len(known_numbers)<len(temp) else 1, sum(known_numbers)/len(known_numbers)


def average_daily_month(minimum, maxumum):
    aver=[average_day(minimum[i], maxumum[i])[1] for i in range(max(len(minimum), len(maxumum)))]
    return average_month(aver)

