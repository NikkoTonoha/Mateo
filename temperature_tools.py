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

    if type(maximum) is str:
        maximum = json.loads(maximum)

    aver = [average_day(minimum[i], maximum[i])[1] for i in range(max(len(minimum), len(maximum)))]
    return average_month(aver)
