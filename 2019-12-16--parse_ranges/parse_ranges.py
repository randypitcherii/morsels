def get_next_range_value(ranges):
    """Generator function that returns the next value in a series from parsed ranges

    Args:
        ranges - list of (start, stop) tuples to build a range from
    Yields:
        next - int value that is next in the series
    """
    for start, stop in ranges:
        while start <= stop:
            yield start
            start += 1

def parse_ranges(ranges_string):
    """ parses string of ranges and returns parsed iterable

    Args:
        ranges_string - string containing series of ranges to parse
            e.g. '1-4,6-6,43-45'
    Returns:
        iterable parsed from the ranges_string
            e.g. [1,2,3,4,6,43,44,45]
    """
    # process input into list of range start/stops
    list_of_range_strings = ranges_string.split(',')
    ranges = []
    for range_string in list_of_range_strings:
        start, stop = range_string.split('-')
        ranges.append((int(start), int(stop)))
    
    return get_next_range_value(ranges)

