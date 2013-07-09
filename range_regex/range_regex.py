# coding=utf8

#  Split range to ranges that has its unique pattern.
#  Example for 12-345:
#
#  12- 19: 1[2-9]
#  20- 99: [2-9]\d
# 100-299: [1-2]\d{2}
# 300-339: 3[0-3]\d
# 340-345: 34[0-5]


def bounded_regex_for_range(min_, max_):
    return r'\b({})\b'.format(regex_for_range(min_, max_))


def regex_for_range(min_, max_):
    """
    > regex_for_range(12, 345)
    '1[2-9]|[2-9]\d|[1-2]\d{2}|3[0-3]\d|34[0-5]'
    """
    subpatterns = []

    start = min_
    for stop in split_to_ranges(min_, max_):
        subpatterns.append(range_to_pattern(start, stop))
        start = stop + 1

    return '|'.join(subpatterns)


def split_to_ranges(min_, max_):
    stops = {max_}

    nines_count = 1
    stop = fill_by_nines(min_, nines_count)
    while min_ <= stop < max_:
        stops.add(stop)

        nines_count += 1
        stop = fill_by_nines(min_, nines_count)

    zeros_count = 1
    stop = fill_by_zeros(max_, zeros_count) - 1
    while min_ < stop < max_:
        stops.add(stop)

        zeros_count += 1
        stop = fill_by_zeros(max_, zeros_count) - 1

    stops = list(stops)
    stops.sort()

    return stops


def fill_by_nines(integer, nines_count):
    return int(str(integer)[:-nines_count] + '9' * nines_count)


def fill_by_zeros(integer, zeros_count):
    return integer - integer % 10 ** zeros_count


def range_to_pattern(start, stop):
    pattern = ''
    any_digit_count = 0

    for start_digit, stop_digit in zip(str(start), str(stop)):
        if start_digit == stop_digit:
            pattern += start_digit
        elif start_digit != '0' or stop_digit != '9':
            pattern += '[{}-{}]'.format(start_digit, stop_digit)
        else:
            any_digit_count += 1

    if any_digit_count:
        pattern += r'\d'

    if any_digit_count > 1:
        pattern += '{{{}}}'.format(any_digit_count)

    return pattern